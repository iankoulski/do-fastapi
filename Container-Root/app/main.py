from fastapi import FastAPI
import logging

app = FastAPI()
logger = logging.getLogger(__name__)

@app.get("/")
async def root():
    print("Request received!")
    logger.info(f"request / endpoint!")
    return {"message": "Hello World"}
