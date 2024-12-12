import uvicorn
import sys
import os
from app.core.security import setup_security
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Secure IPTV Application")

# Configuration CORS
origins = os.getenv('CORS_ALLOW_ORIGINS', 'http://localhost:4200').split(',')
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuration sécurité
setup_security(app)

# Inclusion des routes
app.include_router(router, prefix="/api/v1")

if __name__ == "__main__":
    logger.info("Starting application...")
    uvicorn.run(app, host="0.0.0.0", port=8000)
    logger.info("Application shutdown.")

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'app')))
