from fastapi import FastAPI

from database import Base, engine
from routers import routers

Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url="/nobsdocs")
app.include_router(routers.router)