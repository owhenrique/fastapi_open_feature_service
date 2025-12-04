from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.feature_flags.routers.feature_flag_router import (
    router as feature_flag_router,
)
from app.core.database import create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(title='Open Feature Service', lifespan=lifespan)
app.include_router(feature_flag_router)


@app.get('/')
def read_root():
    return {'message': 'welcome to open feature service api v1'}


@app.get('/healthcheck')
def health_check():
    return {'status': 'ok'}
