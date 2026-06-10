# User Management API - Production-Grade FastAPI Application

A professional, production-ready FastAPI application demonstrating best practices with a layered architecture.

## Architecture Overview

```
app/
├── main.py              # FastAPI app initialization and middleware setup
├── run.py               # Application entry point
├── config.py            # Configuration management
├── models/              # SQLAlchemy ORM models (database schema)
│   └── user.py
├── schemas/             # Pydantic request/response models
│   └── users.py
├── services/            # Business logic layer
│   └── user.py
├── routers/             # API route handlers
│   └── users.py
├── repo/                # Data access layer (repositories)
│   └── repositories.py
└── database/            # Database configuration
    └── db.py
```

```mermaid
flowchart TD

    subgraph API
        R[routers/]
    end

    subgraph Application
        S[services/ controllers]
        SC[schemas/]
    end

    subgraph Persistence
        REP[repositories/]
        MOD[models.py<br/>SQLAlchemy Tables]
    end

    DB[(PostgreSQL / MySQL)]

    R -->|Request Schema| SC
    R --> S

    S -->|Business Logic| REP

    REP --> MOD

    MOD --> DB

    DB --> MOD
    MOD --> REP
    REP --> S

    S -->|Response Schema| SC
    SC --> R
```

## Layered Architecture Benefits

1. **Models Layer**: Defines database schema using SQLAlchemy ORM
2. **Schemas Layer**: Validates request/response data using Pydantic
3. **Repository Layer**: Abstracts database operations
4. **Service Layer**: Contains business logic and validation rules
5. **Router Layer**: Handles HTTP endpoints and dependency injection

## Installation

### Prerequisites
- Python 3.10+
- pip (Python package manager)

### Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure environment (optional):
```bash
# Copy the default .env file
cp .env.example .env
# Edit .env with your configuration
```

## Running the Application

### Development Mode (with auto-reload)

```bash
python run.py
```

Or with uvicorn directly:
```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

### Production Mode


Or with Gunicorn + Uvicorn:
```bash
gunicorn app.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

## Docker Deployment

### Build and Run
```bash
# Build the image
docker build -t user-api:latest .

# Run the container
docker run -p 8000:8000 user-api:latest
```

## API Documentation

Once the application is running, access the interactive documentation:

- **Swagger UI**: http://localhost:8000/api/docs
- **ReDoc**: http://localhost:8000/api/redoc
- **OpenAPI Schema**: http://localhost:8000/api/openapi.json

## API Endpoints

### Health Check
```bash
GET /health
```

### Users Management
```bash
# Create a new user
POST /api/v1/users/
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com"
}

# Get all users (with pagination)
GET /api/v1/users/?skip=0&limit=100

# Get a specific user
GET /api/v1/users/{user_id}

# Update a user
PUT /api/v1/users/{user_id}
Content-Type: application/json

{
  "name": "Jane Doe",
  "email": "jane@example.com"
}

# Delete a user
DELETE /api/v1/users/{user_id}
```

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| DATABASE_URL | sqlite:///./app.db | Database connection string |
| SQL_ECHO | False | Enable SQLAlchemy SQL logging |
| HOST | 127.0.0.1 | Server host |
| PORT | 8000 | Server port |
| WORKERS | 1 | Number of worker processes |
| RELOAD | True | Enable auto-reload on file changes |
| ALLOWED_ORIGINS | * | CORS allowed origins |
| ENVIRONMENT | development | Application environment |

## Database

### Supported Databases
- **SQLite** (default, development): `sqlite:///./app.db`
- **PostgreSQL**: `postgresql://user:password@localhost:5432/dbname`
- **MySQL**: `mysql+pymysql://user:password@localhost:3306/dbname`

### Running Migrations

The application creates tables automatically on startup. For production, use Alembic:

```bash
# Initialize Alembic
alembic init alembic

# Create migration
alembic revision --autogenerate -m "Add users table"

# Apply migrations
alembic upgrade head
```

## Code Quality

### Linting
```bash
flake8 app/
black app/
pylint app/
```

### Type Checking
```bash
mypy app/
```

### Testing
```bash
pytest tests/
```

## Project Structure Best Practices

- **Separation of Concerns**: Each layer has a specific responsibility
- **Dependency Injection**: Services are injected into routes
- **Error Handling**: Centralized exception handling with proper HTTP status codes
- **Configuration Management**: Environment-based configuration
- **Database Abstraction**: Repository pattern for data access
- **API Versioning**: Endpoints prefixed with `/api/v1/`
- **Documentation**: Auto-generated API docs with FastAPI

## Development Workflow

1. **Add a new feature**:
   - Create model in `models/`
   - Define schema in `schemas/`
   - Implement repository in `repo/`
   - Add business logic in `services/`
   - Create routes in `routers/`

2. **Test the feature**:
   - Write unit tests
   - Test with the API docs

3. **Deploy**:
   - Update `.env` for production
   - Use Docker or cloud platform
   - Monitor logs and performance

## Dependencies

- **fastapi**: Web framework
- **uvicorn**: ASGI server
- **sqlalchemy**: ORM
- **pydantic**: Data validation
- **python-dotenv**: Environment variable management

## License

This project is licensed under the MIT License.

## Support

For issues or questions, please refer to the official documentation:
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [SQLAlchemy Docs](https://docs.sqlalchemy.org/)
- [Pydantic Docs](https://docs.pydantic.dev/)
