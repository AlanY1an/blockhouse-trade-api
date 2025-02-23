from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from . import models, schemas, database

router = APIRouter()


@router.post("/orders", response_model=schemas.OrderResponse)
def create_order(order: schemas.OrderCreate = Body(...), db: Session = Depends(database.get_db)):
    new_order = models.Order(**order.dict())  # create new order object
    db.add(new_order)  # add to database
    db.commit()  # commit transaction
    db.refresh(new_order)  # refresh instance, get ID
    return new_order  # return new created order


@router.get("/orders", response_model=list[schemas.OrderResponse])
def get_orders(db: Session = Depends(database.get_db)): 
    return db.query(models.Order).all()  # query all orders

