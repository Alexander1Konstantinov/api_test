from fastapi import FastAPI


app = FastAPI()
books = ["first", "second"]


@app.get("/books")
def root():
    return books
