from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    image_url = Column(String)  # ссылка на картинку товара

    reviews = relationship("Review", back_populates="product")

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    user_name = Column(String, nullable=False)
    rating = Column(Integer, nullable=False)  # от 1 до 5
    comment = Column(String)

    product = relationship("Product", back_populates="reviews")
