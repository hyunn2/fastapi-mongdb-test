from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']


class Item(BaseModel):
    name: str
    price: float


app = FastAPI()


@app.post("/items")
def create_item(item: Item):
    try:
        item_id = db['items'].insert_one(item.dict()).inserted_id
        return {"item_id": str(item_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/items/{item_id}")
def read_item(item_id: str):
    try:
        item = db["items"].find_one({"_id": ObjectId(item_id)})
        if item:
            return item
        else:
            raise HTTPException(status_code=404, detail="Item not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.put("/items/{item_id}")
def update_item(item_id: str, item: Item):
    try:
        updated_item = db["items"].update_one({"_id": ObjectId(item_id)},
                                              {"$set": item.dict()})
        if updated_item.modified_count > 0:
            return {"message": "Item updated successfully"}
        else:
            raise HTTPException(status_code=404, detail="Item not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/items/{item_id}")
def delete_item(item_id: str):
    try:
        deleted_item = db["items"].delete_one({"_id": ObjectId(item_id)})
        if deleted_item.deleted_count > 0:
            return {"message": "Item deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="Item not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))