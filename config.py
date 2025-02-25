import os

DB_USER = os.getenv("DB_USER", "admin")
DB_PASSWORD = os.getenv("DB_PASSWORD", "Mphasis123")
DB_HOST = os.getenv("DB_HOST", "lab-4.cdiwumagq0uz.us-east-1.rds.amazonaws.com")
DB_NAME = os.getenv("DB_NAME", "lab4")

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
