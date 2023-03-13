import os

POSTGRES_USER = os.environ.get("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "postgres")
DATABASE_URL = os.environ.get("DATABASE_URL", "auth_db")
DATABASE_PORT = int(os.environ.get("DATABASE_PORT", "5432"))
POSTGRES_DATABASE = os.environ.get("POSTGRES_DATABASE", "users")

SECRET_KEY = os.environ.get("SECRET_KEY", "alvynabranches")
ALGORITHM = os.environ.get("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRATION_MINUTES = int(os.environ.get("ACCESS_TOKEN_EXPIRATION", 60*24))

TIMEZONE = os.environ.get("Asia/Kolkata")
