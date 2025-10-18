import os
from dotenv import load_dotenv

# Load .env from the project root
dotenv_path = os.path.join(os.path.dirname(__file__), "../.env")
load_dotenv(dotenv_path)

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_ANON_KEY")

if not SUPABASE_URL:
    raise ValueError("SUPABASE_URL environment variable is not set")

if not SUPABASE_KEY:
    raise ValueError("SUPABASE_ANON_KEY environment variable is not set")
