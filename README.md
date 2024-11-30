### AS_Test_API


# Sommaire
### 1- Objective
### 2- Answers
### 3- Achievements
### 4- Installation
### 5- Credits

# 1- Objective

Building a logical representation of Onto-X that preserves ancestor relationships (direct and indirect) and consequently enables reconstructing the hierarchy of entities. In other terms, for a given entity, we want to get all its relationships with the rest of the ontology entities. In addition we want to extract the depth of each relationship.

# 2- Answers
- Principles
    * To create my api, I decided to build a directed graph. It allows me to more easily find the genealogy of each node. I used graph theory

- Decisions
    * I chose the NetworkX python library
    for its ease of use and the fact that it has several functions optimized for this purpose

- Recommandations
    * Improving graph performance
    * Consider a more robust tool such as neo4j
    * Consider graph visualization
    * Improve user experience



# 3- Achievements
    - The API implemented in python 
    - Querybale through a Command Line Interface
    - Expose the traetment via Rest API using FastAPI
    - Docker image of the RestAPI
# 4- Installation
# 5- Credits

In the README, you should try to answer the following questions:

What are the principles you applied
Can you explain the decisions you made and why it is the best approach
What are your recommendations for future work