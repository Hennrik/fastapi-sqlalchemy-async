from fastapi import FastAPI

from source.endpoints import books, stores

app = FastAPI()

app.include_router(books.router, prefix="/book", tags=["books"])
app.include_router(stores.router, prefix="/store", tags=["stores"])

