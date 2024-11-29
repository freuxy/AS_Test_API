from fastapi import FastAPI
from fastapi.responses import JSONResponse
from urllib.parse import unquote
from services.onto_functions import *

app = FastAPI()


@app.get("/")
def get_parents(id: str) -> JSONResponse:
    # Décoder l'ID pour éviter les %20 dans l'URL
    raw_id = unquote(id)
    print(f"Raw decoded ID: {raw_id}")

    graph = load_ontology('./data/onto_x.csv')

    # Vérifier si l'ID existe dans le graphe sous l'une ou l'autre forme (encodée ou non)
    try:
        # Essayez d'abord avec l'ID décodé
        res = get_entity_relationships(graph, raw_id)
    except ValueError as e:
        # Si l'ID n'est pas trouvé, essayez avec l'ID encodé (%20 -> %2520)
        encoded_id = raw_id.replace(' ', '%20')  # Replace spaces with %20 to check encoded ID
        try:
            res = get_entity_relationships(graph, encoded_id)
        except ValueError:
            return JSONResponse(status_code=404, content={"error": f"Entity {id} not found in the ontology."})

    return JSONResponse(status_code=200, content=res)

