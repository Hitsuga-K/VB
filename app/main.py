from fastapi import FastAPI, Request, Depends, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from app.database import Base, engine, SessionLocal
from app.models import Product, Review

# Создаём таблицы
Base.metadata.create_all(bind=engine)

# Создаём приложение
app = FastAPI()

# Подключаем шаблоны и статику
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Сессия БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Маршруты ---
@app.get("/", response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return templates.TemplateResponse("index.html", {"request": request, "products": products})

@app.get("/add-product", response_class=HTMLResponse)
def add_product_form(request: Request):
    return templates.TemplateResponse("add_product.html", {"request": request})

@app.post("/add-product")
def add_product(
    name: str = Form(...),
    description: str = Form(...),
    price: float = Form(...),
    image_url: str = Form(...),
    db: Session = Depends(get_db)
):
    product = Product(name=name, description=description, price=price, image_url=image_url)
    db.add(product)
    db.commit()
    return RedirectResponse("/", status_code=303)

@app.get("/product/{product_id}", response_class=HTMLResponse)
def product_detail(product_id: int, request: Request, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    return templates.TemplateResponse("product_detail.html", {"request": request, "product": product})
