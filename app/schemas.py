from pydantic import BaseModel


# Request
class OrderCreate(BaseModel):
    symbol: str
    price: float
    quantity: int
    order_type: str


# Response
class OrderResponse(OrderCreate):
    id: int  # order ID
