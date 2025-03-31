import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_empty_input():
    response = client.post("/translate", json={"text": ""})
    assert response.json() == {"translated_text": ""}  # Empty input should return empty output.

def test_mixed_case_input():
    response = client.post("/translate", json={"text": "HeLLo"})
    assert response.json() == {"translated_text": "Ellohay"}  # Ensure mixed case input is handled correctly.

def test_invalid_json():
    # Test when the input is not in the correct JSON format
    response = client.post("/translate", data="not a json")
    assert response.status_code == 422  # FastAPI should return a validation error (422 Unprocessable Entity).

def test_non_string_input():
    # Test when the input is a non-string type (like a list or a dictionary)
    response = client.post("/translate", json={"text": 1234})
    assert response.status_code == 422  # FastAPI should return a validation error (422 Unprocessable Entity).

def test_lowercase_consonant():
    response = client.post("/translate", json={"text": "pig"})
    assert response.json() == {"translated_text": "igpay"}

def test_lowercase_vowel():
    response = client.post("/translate", json={"text": "egg"})
    assert response.json() == {"translated_text": "eggay"}

def test_uppercase_consonant():
    response = client.post("/translate", json={"text": "Hello"})
    assert response.json() == {"translated_text": "Ellohay"}

def test_uppercase_vowel():
    response = client.post("/translate", json={"text": "Orange"})
    assert response.json() == {"translated_text": "Orangeay"}

def test_multiple_consonants():
    response = client.post("/translate", json={"text": "Struck"})
    assert response.json() == {"translated_text": "Uckstray"}

def test_multiple_words():
    response = client.post("/translate", json={"text": "Hello world"})
    assert response.json() == {"translated_text": "Ellohay orldway"}

def test_punctuation():
    response = client.post("/translate", json={"text": "Hello, world."})
    assert response.json() == {"translated_text": "Ellohay, orldway."}
