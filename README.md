# FastAPI Sample Application

A simple FastAPI application with CRUD operations for managing items, including comprehensive test cases.

## Features

- **FastAPI** web framework
- **Pydantic** models for data validation
- **CRUD operations** for items (Create, Read, Update, Delete)
- **Comprehensive test suite** using pytest
- **Automatic API documentation** with Swagger UI

## API Endpoints

- `GET /` - Welcome message
- `GET /items` - Get all items
- `GET /items/{item_id}` - Get specific item by ID
- `POST /items` - Create new item
- `PUT /items/{item_id}` - Update existing item
- `DELETE /items/{item_id}` - Delete item

## Setup Instructions

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   python main.py
   ```
   Or using uvicorn directly:
   ```bash
   uvicorn main:app --reload
   ```

3. **Access the application:**
   - API: http://localhost:8000
   - Interactive API docs (Swagger UI): http://localhost:8000/docs
   - Alternative API docs (ReDoc): http://localhost:8000/redoc

## Running Tests

Run the test suite:
```bash
pytest test_main.py -v
```

Or run with coverage:
```bash
pytest test_main.py --cov=main -v
```

## Test Cases

The test suite includes:
- Root endpoint test
- Item creation and retrieval
- Getting non-existent items
- Item updates
- Item deletion

## Example Usage

### Create an item:
```bash
curl -X POST "http://localhost:8000/items" \
     -H "Content-Type: application/json" \
     -d '{
       "id": 1,
       "name": "Sample Item",
       "description": "A sample item",
       "price": 29.99,
       "is_available": true
     }'
```

### Get all items:
```bash
curl -X GET "http://localhost:8000/items"
```

### Get specific item:
```bash
curl -X GET "http://localhost:8000/items/1"
```

## Project Structure

```
pythonapp/
├── main.py          # FastAPI application
├── test_main.py     # Test cases
├── requirements.txt # Dependencies
└── README.md        # This file
```
