from fastapi import FastAPI
import uvicorn

app = FastAPI()

books =['first', 'second']

@app.get("/books")
def root():
    return books
