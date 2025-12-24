from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    description: str | None = None
    price: float
    image_url: str | None = None

class ProductCreate(ProductBase):
    pass

class ProductRead(ProductBase):
    id: int
    class Config:
        from_attributes = True

class ReviewBase(BaseModel):
    user_name: str
    rating: int
    comment: str | None = None

class ReviewCreate(ReviewBase):
    product_id: int

class ReviewRead(ReviewBase):
    id: int
    product_id: int
    class Config:
        from_attributes = True
