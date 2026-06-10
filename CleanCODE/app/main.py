import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse


from app.routers.users import user_router
from app.database.db import Base, engine # Base class and engine from our db.py

load_dotenv()


# Initialize database tables so our models are created in the database
Base.metadata.create_all(bind=engine)


# Create FastAPI application
app = FastAPI(
    title="User Management API",
    description="Production-grade FastAPI application with layered architecture",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
)

# CORS Middleware configuration
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "*").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Health check endpoint
@app.get("/health", tags=["Health"])
def health_check():
    """Health check endpoint"""
    return JSONResponse(
        status_code=200, content={"status": "healthy", "version": "1.0.0"}
    )


# Root endpoint
@app.get("/", tags=["Root"])
def read_root():
    """Root endpoint with API information"""
    return {
        "message": "Welcome to User Management API",
        "version": "1.0.0",
        "docs": "/api/docs",
        "health": "/health",
    }


# Include routers
app.include_router(user_router)


# Exception handlers
@app.exception_handler(ValueError)
async def value_error_handler(request, exc):
    return JSONResponse(status_code=400, content={"detail": str(exc)})


@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    return JSONResponse(status_code=500, content={"detail": "Internal server error"})
