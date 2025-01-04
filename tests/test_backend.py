import pytest
from backend.app import app

def test_analyze_endpoint():
    client = app.test_client()
    response = client.post('/analyze', data={"image": (BytesIO(b"test image data"), "test.jpg")})
    assert response.status_code == 200