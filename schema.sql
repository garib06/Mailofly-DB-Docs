-- ============================================================
-- Supabase Relational Schema: profiles & projects (1 : N)
-- ============================================================

-- 1. Helper Extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- ============================================================
-- TABLE 1: public.profiles
-- Represents user profile data linked 1:1 with auth.users
-- ============================================================
CREATE TABLE IF NOT EXISTS public.profiles (
    id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
    username TEXT UNIQUE NOT NULL,
    full_name TEXT,
    avatar_url TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now()),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now()),

    -- Basic constraints
    CONSTRAINT username_min_length CHECK (char_length(username) >= 3)
);

-- ============================================================
-- TABLE 2: public.projects
-- Represents projects owned by a user profile (1:N relationship)
-- ============================================================
CREATE TABLE IF NOT EXISTS public.projects (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    owner_id UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
    name TEXT NOT NULL,
    slug TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'active' CHECK (status IN ('active', 'archived', 'draft')),
    created_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now()),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now()),

    -- Prevent duplicate slugs for the same owner
    CONSTRAINT unique_project_slug_per_owner UNIQUE (owner_id, slug)
);

-- ============================================================
-- INDEXES for Query Optimization
-- ============================================================
CREATE INDEX IF NOT EXISTS idx_projects_owner_id ON public.projects(owner_id);
CREATE INDEX IF NOT EXISTS idx_projects_status ON public.projects(status);

-- ============================================================
-- AUTOMATIC TIMESTAMP TRIGGERS
-- ============================================================
CREATE OR REPLACE FUNCTION public.handle_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = timezone('utc'::text, now());
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS set_profiles_updated_at ON public.profiles;
CREATE TRIGGER set_profiles_updated_at
    BEFORE UPDATE ON public.profiles
    FOR EACH ROW EXECUTE FUNCTION public.handle_updated_at();

DROP TRIGGER IF EXISTS set_projects_updated_at ON public.projects;
CREATE TRIGGER set_projects_updated_at
    BEFORE UPDATE ON public.projects
    FOR EACH ROW EXECUTE FUNCTION public.handle_updated_at();

-- ============================================================
-- AUTOMATIC PROFILE CREATION ON SUPABASE AUTH SIGN-UP
-- ============================================================
CREATE OR REPLACE FUNCTION public.handle_new_user()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO public.profiles (id, username, full_name, avatar_url)
    VALUES (
        NEW.id,
        COALESCE(NEW.raw_user_meta_data->>'username', split_part(NEW.email, '@', 1)),
        COALESCE(NEW.raw_user_meta_data->>'full_name', ''),
        COALESCE(NEW.raw_user_meta_data->>'avatar_url', '')
    );
    RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

DROP TRIGGER IF EXISTS on_auth_user_created ON auth.users;
CREATE TRIGGER on_auth_user_created
    AFTER INSERT ON auth.users
    FOR EACH ROW EXECUTE FUNCTION public.handle_new_user();

-- ============================================================
-- ROW LEVEL SECURITY (RLS) POLICIES
-- ============================================================
ALTER TABLE public.profiles ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.projects ENABLE ROW LEVEL SECURITY;

-- Profiles: Anyone authenticated can read profiles; users can only update their own
CREATE POLICY "Public profiles are viewable by everyone" 
    ON public.profiles FOR SELECT 
    USING (true);

CREATE POLICY "Users can insert their own profile" 
    ON public.profiles FOR INSERT 
    WITH CHECK (auth.uid() = id);

CREATE POLICY "Users can update their own profile" 
    ON public.profiles FOR UPDATE 
    USING (auth.uid() = id);

-- Projects: Users can only select, create, update, and delete their own projects
CREATE POLICY "Users can view their own projects" 
    ON public.projects FOR SELECT 
    USING (auth.uid() = owner_id);

CREATE POLICY "Users can create their own projects" 
    ON public.projects FOR INSERT 
    WITH CHECK (auth.uid() = owner_id);

CREATE POLICY "Users can update their own projects" 
    ON public.projects FOR UPDATE 
    USING (auth.uid() = owner_id);

CREATE POLICY "Users can delete their own projects" 
    ON public.projects FOR DELETE 
    USING (auth.uid() = owner_id);
