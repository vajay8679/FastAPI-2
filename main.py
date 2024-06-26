from unittest.util import _MAX_LENGTH
from fastapi import FastAPI, Query, Form, File, UploadFile, HTTPException
from enum import Enum
from typing import Union
from pydantic import BaseModel

app = FastAPI()

# app_name = FastAPI()

class schema1(BaseModel):
    name:str
    Class:str
    roll_no:int

class ModelName(str, Enum):
    one = "one"
    two = "two"
    three = "three"

@app.get("/")
async def root():
    return {"message": "Hello World"}



@app.get("/hello")
async def root():
    return {"message": "Hello World new"}



@app.get("/item/{item}")
async def path_func(item):
    item_var = {"Path variable ": item}
    return (item_var)


@app.get("/query")
# async def query_func(name: str, roll_no:Union[int,None]=None):
async def query_func(name: Union[str,None]=None, roll_no:Union[str,None]=Query(default=None,min_length=3,max_length=4)):
    item_var = {"Name": name,"Roll no.":roll_no}
    return item_var


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name.value:
        return {"model_name": model_name, "message": "Calling one"}

    if model_name.value == "two":
        return {"model_name": model_name, "message": "Calling two"}

    return {"model_name": model_name, "message": "Calling three"}


@app.post("/items/")
async def create_item(item: schema1):
    return item



class Ajay(BaseModel):
    one: str
    two: str
    three: int


# form data
@app.post("/form/data")
async def form_data(username:str = Form(),password:str = Form()):
# async def form_data(item:Ajay):
    return ({"username ": username,"password ": password})
    # return ({"item": item})



# file upload
@app.post("/file/upload")
async def file_bytes_len(file:bytes = File()):
# async def form_data(item:Ajay):
    return ({"file ": len(file)})


@app.post("/upload/file")
async def file_upload(file:UploadFile):
    # return ({"file ": file})
    return ({"file ": file.filename,"file_content_name":file.content_type})


@app.post("/form/data/filedata")
async def file_upload(file1:UploadFile, file2:bytes = File(), name:str = Form()):
    return ({"file1 ": file1.filename,"file_length":len(file2), "name":name})


items = [1,2,3,4,5]
# error handling
@app.get("/error/handling")
async def handle_error(item: int):
    if item not in items:
        return HTTPException(status_code = 400, detail="item is not equal to  2 try another value !!")
    return  {"value":item}