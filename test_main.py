from fastapi.testclient import TestClient
from fastapi import status
from main import app


client = TestClient(app=app)
def test_first1():
    response = client.get('/test1')

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"msg": "My first test"}

def test_first2():
    response = client.post('/post_test', json={"one": "1", "two": "2", "three": 3})

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"one": "1", "two": "2", "three": 3}
