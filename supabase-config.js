import { createClient } from 'https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/+esm';

const SUPABASE_URL = 'https://pjxsweqmmxsrhixxsoyc.supabase.co';
const SUPABASE_KEY = 'sb_publishable_gbvNpQbP1fje-ev7p9x_Jw_Hk-PZoQn';

export const supabase = createClient(SUPABASE_URL, SUPABASE_KEY);
