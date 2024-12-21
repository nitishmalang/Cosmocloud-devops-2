import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from redis import Redis, ConnectionError

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)


try:
    redis_uri = os.getenv("REDIS_URI", "redis://localhost:6379")  
    client = Redis.from_url(redis_uri, decode_responses=True)
    
    client.ping()
except ConnectionError as e:
    print(f"Error connecting to Redis: {e}")
    client = None  


@app.get("/")
def read_root():
    
    if client is None:
        raise HTTPException(status_code=500, detail="Redis connection failed")

    try:
       
        hits = client.incr("hits")
        return {"hits": hits}
    except Exception as e:
        
        raise HTTPException(status_code=500, detail=f"Error interacting with Redis: {str(e)}")

