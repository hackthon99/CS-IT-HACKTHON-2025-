from fastapi import FastAPI,Request
from pydantic import BaseModel
from typing import List
from pymongo import MongoClient
from bson import json_util
import json # to convert bson file to json file

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


# Allowing requests from all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows requests from all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)


@app.get("/") # defining the root endpoint ("/") of the API
def read_root():
    diary = {}
    for i, document in enumerate(collection.find()):
        document['_id'] = str(document['_id'])  # Convert ObjectId to string
        diary[f"doc_{i+1}"] = document
    return {"data": diary}
@app.post("/insert")
async def insert(request: Request):
    try:
        body = await request.json()  # or body = await request.json()
        collection.insert_one(body)
        return {"message": "Document inserted successfully", "data": body}
    except Exception as e:
        print("Error occurred:", str(e))
        return {"error": str(e)}

    
