# Jalanin Backend

A FastAPI backend with Supabase integration and ML capabilities.

## Setup

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Set up environment variables in `.env`:

   - SUPABASE_URL: Your Supabase project URL
   - SUPABASE_ANON_KEY: Your Supabase anon key
   - SUPABASE_DATABASE_URL: Your Supabase database URL (get from Supabase dashboard)

3. Run the server:
   ```bash
   python -m uvicorn src.main:app --reload
   ```

## Development

- The server runs on http://localhost:8000
- API docs available at http://localhost:8000/docs
