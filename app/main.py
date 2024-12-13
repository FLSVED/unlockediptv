import sys
import os

# Add the parent directory 'unlockediptv' to the import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import uvicorn
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.security import setup_security
from app.api.routes import router

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the FastAPI application
app = FastAPI(title="Secure IPTV Application")

# CORS configuration
origins = os.getenv('CORS_ALLOW_ORIGINS', 'http://localhost:4200').split(',')
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Security configuration
setup_security(app)

# Include the routes
app.include_router(router, prefix="/api/v1")

# Main entry point
if __name__ == "__main__":
    logger.info("Starting application...")
    uvicorn.run(app, host="0.0.0.0", port=8000)
    logger.info("Application shutdown.")
