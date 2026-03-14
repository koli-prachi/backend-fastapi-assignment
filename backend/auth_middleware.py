from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from backend.auth import verify_token
from backend.security import require_admin

security = HTTPBearer()

# Get logged-in user
def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):

    token = credentials.credentials
    payload = verify_token(token)

    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid token")

    return payload


# Admin-only dependency
def get_admin_user(user = Depends(get_current_user)):

    require_admin(user)

    return user