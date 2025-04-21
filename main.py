from fastapi import FastAPI # for creating the FastAPI app
from pydantic import BaseModel # for data validation and serialization 
#(it helps in formation of input and output data models for the API)
from typing import List #for type hinting

app = FastAPI() # creating an instance of FastAPI (creating the app)

# creating a class with help of BaseModel for the input data model

class Tea(BaseModel):
    id : int # id of the tea
    name : str # name of the tea
    origin : str # origin of the tea
    

# teas  = [] # list to store the tea data

# here a teas list with basemodel

teas : list[Tea] = [] # this means that teas is a list of Tea class objects (it will sotre the tea data in the form of class objects with index  0,1,2...)
# teas is the name of the list and list[Tea] is the type of the list (like it will store which type of data)
# so in above example it is storing list of list[Tea] (which is a class object)

@app.get("/") # defining the root endpoint ("/") of the API
# the functions below it will run when on api calls the root with "/" 
def read_root(): # defining the function to handle the root endpoint
    # this function will return a welcome message when the root endpoint is called
    return {"message": "Welcome to the Tea API!"}
