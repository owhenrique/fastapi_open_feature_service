from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.routers import feature_flags
from app.models.feature_flag import create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(title='Open Feature Service', lifespan=lifespan)
app.include_router(feature_flags.router)


@app.get('/')
def read_root():
    return {'message': 'welcome to open feature service api v1'}


@app.get('/health')
def health_check():
    return {'status': 'ok'}
