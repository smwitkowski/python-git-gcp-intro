from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
async def get_current_time(name: str):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"message": f"Hello, {name}! The current time is: {current_time}"}