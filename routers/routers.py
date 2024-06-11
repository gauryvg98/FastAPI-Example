from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import Item as ItemModel
from schemas import Item

router = APIRouter()

@router.get("/")
def health():
    return {"status" : "this service is healthy @ " + datetime.now().__str__()}

@router.get("/item", response_model=List[ItemModel])
def item_get(db: Session = Depends(get_db)):
    resp = db.query(Item).all()
    return resp

@router.post("/item", response_model=ItemModel)
def item_create(item: ItemModel, db: Session = Depends(get_db)):
    db_item = Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

