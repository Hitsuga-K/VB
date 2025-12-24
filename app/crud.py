def get_products(db: Session):
    return db.query(models.Product).all()

def create_product(db: Session, product: models.Product):
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def get_reviews(db: Session, product_id: int):
    return db.query(models.Review).filter(models.Review.product_id == product_id).all()

def create_review(db: Session, review: models.Review):
    db.add(review)
    db.commit()
    db.refresh(review)
    return review
