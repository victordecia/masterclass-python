# Masterclass Test

1. Lowercase consonant. Write a function that performs this translation (pig -> igpay) and write a test that validates the function

2. Lowercase vowel. Modify the function to handle this translation (egg -> eggay) and write a test that validates that this and all previous test pass.

3. Uppercase & multiple consonants. Modify the function to handle this translation (Hello -> Ellohay) and write a test that validates that this and all previous test pass. 

4. Uppercase vowel. Modify the function to handle this translation (Orange -> Orangeay) and write a test that validates that this and all previous test pass.

5. Multiple consonants. Modify the function to handle this translation (Struck -> Uckstray) and write a test that validates that this and all previous test pass.

6. Multiple words. Modify the function to handle this translation (Hello world -> Ellohay orldway) and write a test that validates that this and all previous test pass.

7. Punctuation. Modify the function to handle this translation (Hello, world. -> Ellohay, orldway.) and write a test that validates that this and all previous test pass.

# FastAPI Application

This is a simple FastAPI application. Below are the instructions for setting up, running, and testing the app locally, along with installing the necessary dependencies.

## Prerequisites

Before you begin, make sure you have the following installed on your machine:

- [Python 3.7+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/), which is Python's package manager.

## 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/victordecia/masterclass-python.git
cd masterclass-python
```

## 2. Create a Virtual Environment (Recommended)

It's highly recommended to create a virtual environment to manage your project dependencies.

### For macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### For Windows:

```bash
python -m venv venv
.\venv\Scripts\activate
```

Once activated, your terminal prompt will show the virtual environment name.

## 3. Install Dependencies

```bash
pip install fastapi uvicorn pytest httpx
```

This will install the following core dependencies:
- `FastAPI`: The web framework.
- `Uvicorn`: The ASGI server to run the app.
- `pytest`: The testing framework.

## 4. Running the Application Locally

Now that the dependencies are installed, you can run the FastAPI application.

### Run the FastAPI Application

To start the application, run the following command in the terminal:

```bash
uvicorn main:app --reload
```

- `--reload` enables auto-reloading during development, so changes to the code take effect immediately.

You should see output like this:

```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

Open your browser and navigate to `http://127.0.0.1:8000` to view your FastAPI application.

Additionally, FastAPI automatically generates interactive API documentation:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 5. Running Tests Locally

### Install `pytest` (if not installed yet)

If `pytest` isn't installed yet, you can install it by running:

```bash
pip install pytest
```

### Run the Tests

To run the tests, simply execute:

```bash
pytest -v test_main.py
```

## 6. Deactivating the Virtual Environment (Optional)

Once you're done, you can deactivate the virtual environment by running:

```bash
deactivate
```

## Troubleshooting

- If you encounter any issues while installing dependencies, try upgrading `pip` to the latest version:

  ```bash
  pip install --upgrade pip
  ```

- Ensure you are using Python 3.7+:

  ```bash
  python3 --version
  ```

- If `pytest` is not found, ensure it's installed in the active virtual environment. Run:

  ```bash
  pip install pytest
  ```