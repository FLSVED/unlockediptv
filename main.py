import uvicorn
import sys
import os
from app.core.security import setup_security
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.security import setup_security
from app.api.routes import router

app = FastAPI(title="Secure IPTV Application")

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuration sécurité
setup_security(app)

# Inclusion des routes
app.include_router(router, prefix="/api/v1")

if __name__ == "__main__":
    
    uvicorn.run(app, host="0.0.0.0", port=8000)
    input("Appuyez sur Entrée pour fermer...")

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'app')))



