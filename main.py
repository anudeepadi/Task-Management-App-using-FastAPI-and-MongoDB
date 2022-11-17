from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.router import router
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",  
    "http://localhost:5000"  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/v1", tags=["tasks"])
