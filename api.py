from fastapi import FastAPI, Body

app = FastAPI()

@app.post("/calculate")
def calculate(
    num1: float = Body(),  # FastAPI сам разберёт JSON
    num2: float = Body()
):
    return {"result": num1 + num2}