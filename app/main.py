# import fastapi
from fastapi import FastAPI
from . database import engine
from .database import Base
from .routers import post, user, auth, vote
from .config import settings

from fastapi.middleware.cors import CORSMiddleware

origins = ["*"]
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

# Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "hello, world"}
    
