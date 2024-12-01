#import pandas as pd
#import duckdb
import networkx as nx
import csv


def load_ontology(file_path:str):
    """
        Charger les données et construire un graphe orienté.
        1) Charger le fichier CSV
        2) Créer un DiGraph à partir des données chargées
        :param file_path: un string contenant le chemain vers le fichier csv
        :return: Digraph
    """
    graph = nx.DiGraph()
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)

        for row in reader:
            entity_id = row['Class ID']
            parents = row['Parents'].split('|')

            graph.add_node(entity_id, label=row['Preferred Label'])
            for parent in parents:
                if parent.strip():
                    graph.add_edge(parent.strip(), entity_id)
    return graph


def get_entity_relationships(graph, entity_id)-> dict:
    """
        Retourner les ancêtres (directs et indirects) et leurs profondeurs.
        1) Renvoie le dictionnaire des relations
        2) Lève une erreur si l'id n'existe pas
        :param graph: un graph comportant toute les relations
        :param entity_id: Un string  comportant l'id de l'ontologie recherché
        :return: dict
    """

    if entity_id not in graph:
        raise ValueError(f"Entity {entity_id} not found in the ontology.")

    # Trouver tous les ancêtres et leurs distances
    relationships = nx.single_source_shortest_path_length(graph.reverse(), entity_id)
    return relationships