from fastapi import FastAPI
from fastapi.responses import JSONResponse
from services.onto_functions import *

app = FastAPI()

"""

@app.get("/")
def test() -> JSONResponse:
    return JSONResponse(status_code=200, content="Salut  test!!")

"""

@app.get("/")
def get_parents(id:str)-> JSONResponse:
    graph = load_ontology('./data/onto_x.csv')
    res = get_entity_relationships(graph, id)  # "http://entity/CST/HYPOCHLOREM")
    return JSONResponse(status_code=200, content=res)

