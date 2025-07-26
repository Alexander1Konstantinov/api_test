from fastapi import Body, FastAPI


app = FastAPI()


@app.post("/calculate")
def calculate(num1: float = Body(), num2: float = Body()):  # FastAPI сам разберёт JSON
    return {"result": num1 + num2}
