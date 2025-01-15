from fastapi import FastAPI
import logging
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
logger = logging.getLogger(__name__)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    print("Request received!")
    logger.info(f"request / endpoint!")
    return {"message": "Hello World"}
