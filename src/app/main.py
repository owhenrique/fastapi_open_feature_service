from fastapi import FastAPI

app = FastAPI(title='Open Feature Service')

@app.get('/')
def read_root():
    return {'message': 'welcome to open feature service api v1'}

@app.get('/health')
def health_check():
    return {'status': 'ok'}