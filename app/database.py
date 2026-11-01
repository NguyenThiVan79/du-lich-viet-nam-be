
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, URL
from sqlalchemy.orm import declarative_base, sessionmaker

# Đọc thông tin từ file .env
load_dotenv()

# Cấu hình kết nối PostgreSQL
database_url = URL.create(
    drivername="postgresql+psycopg",
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT", "5432")),
    database=os.getenv("DB_NAME")
)

# Tạo kết nối
engine = create_engine(database_url)

# Quản lý phiên làm việc với database
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


# Đóng kết nối sau khi sử dụng
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
