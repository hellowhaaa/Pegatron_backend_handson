from unittest.mock import patch
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)


def test_empty_name():
    with patch("src.controllers.users.create_user") as mock_get_user:
        mock_get_user.return_value = None
        response = client.post(
        "/users",
        json={"name": "", "age": 123}
        )
        assert response.status_code == 422
        assert response.json() == {"detail": 'name: Value error, Name cannot be empty or blank'}
        

def test_older_age():
    with patch("src.controllers.users.create_user") as mock_get_user:
        mock_get_user.return_value = None
        response = client.post(
        "/users",
        json={"name": "Lily", "age": 999}
        )
        assert response.status_code == 422
        assert response.json() == {"detail": 'age: Value error, Age must be in normal range (0-150)'}