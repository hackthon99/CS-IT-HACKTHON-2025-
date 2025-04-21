from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from pymongo import MongoClient
# from pymongo import ServerApi
from urllib.parse import quote_plus # just to make the url correct


username = quote_plus("KunalBavdhane") # Use quote_plus to encode special characters in the username
password = quote_plus("Kunal12345%") # Use quote_plus to encode special characters in the password
uri = f"mongodb+srv://{username}:{password}@cluster0.2r5vfqe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri) # creating a client to connect to the MongoDB database
database = client["TEST_DATABASE"] # creating a database object to connect to the database
collection = database["TEST_COLLECTION"] # creating a collection object to connect to the collection in the database
# for document in collection.find():
#     print(document)
collection.insert_one({"name": "Kunal", "age": 23}) # inserting a document into the collection (just for testing purpose)

app = FastAPI() # creating an instance of FastAPI (creating the app)

@app.get("/") # defining the root endpoint ("/") of the API
def read_root():
    # this function will return a welcome message when the root endpoint is called
    return {list(collection.find())} # send all collection in the form of list means our whole mongodb data

# @app.post("/insert")
# async def insert(request : Request):
#     body = await request.json()
#     collection.insert_one(body) # inserting the document into the collection
#     return {"message": "Document inserted successfully :{body}"} 
    
