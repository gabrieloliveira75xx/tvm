import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Add this line to specify the schema
    SQLALCHEMY_ENGINE_OPTIONS = {"connect_args": {"options": "-c search_path=chatbot_schema"}}