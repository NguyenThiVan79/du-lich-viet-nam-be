
# # from fastapi import FastAPI
# # from fastapi.middleware.cors import CORSMiddleware

# # app = FastAPI(
# #     title="Du Lich Viet Nam API",
# #     description="Backend website giới thiệu các địa điểm du lịch Việt Nam",
# #     version="1.0.0"
# # )

# # # Cho phép Frontend React truy cập Backend
# # app.add_middleware(
# #     CORSMiddleware,
# #     allow_origins=["http://localhost:5173"],
# #     allow_credentials=True,
# #     allow_methods=["*"],
# #     allow_headers=["*"],
# # )

# # # API kiểm tra kết nối
# # @app.get("/api/hello")
# # def hello():
# #     return "Xin chào"

# # # Đăng ký router
# # app.include_router(
# #     hello.router,
# #     prefix="/api",
# #     tags=["Hello"]
# # )

# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# # Import router hello
# from app.routers.hello import router as hello_router

# app = FastAPI(
#     title="Du Lich Viet Nam API",
#     description="Backend website giới thiệu các địa điểm du lịch Việt Nam",
#     version="1.0.0"
# )

# # Cấu hình CORS cho React
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:5173"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Đăng ký router
# app.include_router(
#     hello_router,
#     prefix="/api",
#     tags=["Hello"]
# )
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine

# Import model để SQLAlchemy nhận diện bảng
from app.models.user import User

# Import routers
from app.routers import hello, auth


app = FastAPI(
    title="Du Lich Viet Nam API",
    description="Backend website giới thiệu các địa điểm du lịch Việt Nam",
    version="1.0.0"
)


# Cấu hình CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Tạo bảng nếu chưa tồn tại
Base.metadata.create_all(bind=engine)


# Đăng ký router
app.include_router(
    hello.router,
    prefix="/api",
    tags=["Hello"]
)

app.include_router(
    auth.router,
    prefix="/api/auth",
    tags=["Authentication"]
)


@app.get("/")
def root():
    return {
        "message": "Du Lich Viet Nam API is running"
    }