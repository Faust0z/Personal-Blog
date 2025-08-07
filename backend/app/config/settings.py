import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    raise FileNotFoundError(".env file not found. Please create one before running the app.")

load_dotenv()
DB_URI = os.getenv("DB_URI", "sqlite:///blog.db")