from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings



SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"
# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:BllM725Tnn@127.0.0.1:5433/fastapi'


# engine responsable to create engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
# try:
#     conn = psycopg2.connect("host=localhost port=5433 dbname=fastapi user=postgres password=BllM725Tnn connect_timeout=10 sslmode=prefer", cursor_factory=RealDictCursor)
#     # we have access
#     cursor = conn.cursor()
#     print("database conection was seccesfull")
# except Exception as error:
#     print('not connect')
#     print(error)
#     time.sleep(2)