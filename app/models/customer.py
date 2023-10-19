from pydantic import BaseModel

class CustomerBase(BaseModel):
    name: str
    email: str

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase):
    class Config:
        orm_mode = True