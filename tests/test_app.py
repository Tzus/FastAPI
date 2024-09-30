from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_read_root_deve_retornar_ok_e_hello_world():
    client = TestClient(app)  # Arrange (organização)
    response = client.get('/')  # Act (ação)
    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Hello World!'}


def test_aula_02_deve_retornar_ola_mundo_html():
    client = TestClient(app)
    response = client.get('/aula_02')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == '<h1> Olá Mundo </h1>'
