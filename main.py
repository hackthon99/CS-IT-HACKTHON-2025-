from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from urllib.parse import quote_plus
from bson import json_util
import json

app = FastAPI()

# ✅ Add CORS middleware at the top immediately after creating app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For testing only; restrict to frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Now safely configure MongoDB connection
username = quote_plus("KunalBavdhane")
password = quote_plus("Kunal12345%")
uri = f"mongodb+srv://{username}:{password}@cluster0.2r5vfqe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri)
database = client["TEST_DATABASE"]
collection = database["TEST_COLLECTION"]

# Optional: Test insert (you can comment this out later)
collection.insert_one({"name": "Kunal", "age": 23})

@app.get("/")
def read_root():
    diary = {}
    for i, document in enumerate(collection.find()):
        document['_id'] = str(document['_id'])
        diary[f"doc_{i+1}"] = document
    return {"data": diary}

@app.post("/insert")
async def insert(request: Request):
    try:
        body = await request.json()
        result = collection.insert_one(body)
        return {
            "message": "Inserted successfully",
            "inserted_id": str(result.inserted_id)  # Convert ObjectId to string
        }
    except Exception as e:
        return {"error": str(e)}
