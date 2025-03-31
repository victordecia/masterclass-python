from fastapi import FastAPI
from routes.translate_route import router

app = FastAPI()

app.include_router(router)
