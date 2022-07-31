"""CalBalt Description"""
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """Root route"""
    return {"message": "Hello World"}

