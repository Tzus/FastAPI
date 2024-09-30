from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK)
def read_root():
    return {'message': 'Hello World!'}


@app.get('/aula_2', response_class=HTMLResponse)
def aula_02():
    return '<h1> Olá Mundo </h1>'
