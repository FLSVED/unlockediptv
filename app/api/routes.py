from fastapi import APIRouter

# Import other necessary modules
from .endpoints import items, users

router = APIRouter()

# Include other routers
router.include_router(items.router, prefix="/items", tags=["items"])
router.include_router(users.router, prefix="/users", tags=["users"])

@router.get("/")
async def read_root():
    return {"message": "Welcome to Secure IPTV Application API"}
