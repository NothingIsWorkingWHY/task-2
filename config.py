import os
from dotenv import load_dotenv

load_dotenv()  # reads .env into environment variables

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{os.getenv('MARIADB_USER')}:"
        f"{os.getenv('MARIADB_PASSWORD')}@{os.getenv('DB_HOST', 'localhost')}:"
        f"{os.getenv('DB_PORT', '3306')}/{os.getenv('MARIADB_DATABASE')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False