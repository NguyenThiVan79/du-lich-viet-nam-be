
from sqlalchemy import text
from app.database import engine

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version()"))
        print("Kết nối PostgreSQL thành công!")
        print(result.fetchone()[0])

except Exception as error:
    print("Kết nối PostgreSQL thất bại!")
    print(error)
