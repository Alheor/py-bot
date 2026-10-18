from fastapi import FastAPI
from src.adapter.http.api import webhook_action
from src.infrastructure.persistence.mappers import start_mappers

app = FastAPI()
app.include_router(webhook_action.router)

start_mappers()

