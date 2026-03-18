import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        from app import students
        students.clear()
        yield client


def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json()["status"] == "healthy"


def test_register_student(client):
    resp = client.post("/students", json={"name": "Ada Lovelace", "email": "ada@eduvos.co.za", "course": "Computer Science"})
    assert resp.status_code == 201
    data = resp.get_json()
    assert data["name"] == "Ada Lovelace"
    assert data["id"] == 1


def test_duplicate_email(client):
    client.post("/students", json={"name": "Ada", "email": "ada@eduvos.co.za"})
    resp = client.post("/students", json={"name": "Bob", "email": "ada@eduvos.co.za"})
    assert resp.status_code == 409


def test_missing_fields(client):
    resp = client.post("/students", json={"name": "Ada"})
    assert resp.status_code == 400


def test_get_students(client):
    client.post("/students", json={"name": "Ada", "email": "ada@eduvos.co.za"})
    resp = client.get("/students")
    assert resp.status_code == 200
    assert len(resp.get_json()) == 1


def test_get_student_not_found(client):
    resp = client.get("/students/999")
    assert resp.status_code == 404
