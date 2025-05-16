from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.api import car
from app.db.database import Base, engine

app = FastAPI(title="ToyotaShop API")

Base.metadata.create_all(bind=engine)

@app.get("/", include_in_schema=False)
def root_redirect():
    return RedirectResponse(url="/docs")

app.include_router(car.router, prefix="/api")
