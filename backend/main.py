import fastapi
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from db_utils import *
from pydantic import BaseModel


app = fastapi.FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Guest(BaseModel):
    first_name: str
    last_name: str
    phone: str
    status: str
    how_much: int

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/orders")
async def get_orders():
    return get_todo_table()

@app.post("/add_guest")
async def add_order(guest: Guest):
    return insert_order(guest.first_name, guest.last_name, guest.phone, guest.status, guest.how_much)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8001)