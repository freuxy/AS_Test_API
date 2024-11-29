from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/")
def visit() -> JSONResponse:
    return JSONResponse(status_code=200, content="Salut !!")

