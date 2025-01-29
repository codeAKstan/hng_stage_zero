# HNG12 Stage 0 Task - Public API (Django)

This is a simple public API built with Django that returns basic information in JSON format.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/codeAKstan/hng_stage_zero.git

2. Install dependecies
    ``` bash
    pip install -r requirements.txt

3. Run the development server:
    ``` bash
    python manage.py runserver

4. Endpoint: GET /api/info/
    ``` bash
    http://127.0.0.1:8000/api/info/


## API Documentation
- **Endpoint**: `GET /api/info/`
- **Response**:
    ```json
    {
        "email": "anigbomosesstan@gmail.com",
        "current_datetime": "2025-01-29T21:26:29.382403Z",
        "github_url": "https://github.com/codeAKstan/hng_stage_zero.git"
    }


## Example Usage
```
curl https://hng-stage-zero-4uv6.onrender.com/api/info/
```

## Backlink
https://hng.tech/hire/python-developers