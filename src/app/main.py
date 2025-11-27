from fastapi import FastAPI

from app.api.routers import feature_flags

app = FastAPI(title='Open Feature Service')
app.include_router(feature_flags.router)


@app.get('/')
def read_root():
    return {'message': 'welcome to open feature service api v1'}


@app.get('/health')
def health_check():
    return {'status': 'ok'}
