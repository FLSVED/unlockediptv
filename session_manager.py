import logging
from datetime import datetime, timedelta
from jose import jwt
from app.core.security import SECRET_KEY, ALGORITHM

class SessionManager:
    def __init__(self, config_manager):
        self.config_manager = config_manager
        self.sessions = {}

    def create_session(self, user_id):
        expires = datetime.utcnow() + timedelta(minutes=30)
        session_token = jwt.encode({"user_id": user_id, "exp": expires}, SECRET_KEY, algorithm=ALGORITHM)
        self.sessions[session_token] = {"user_id": user_id, "expires": expires}
        return session_token

    def validate_session(self, session_token):
        try:
            payload = jwt.decode(session_token, SECRET_KEY, algorithms=[ALGORITHM])
            user_id = payload["user_id"]
            if session_token in self.sessions and self.sessions[session_token]["expires"] > datetime.utcnow():
                return user_id
            else:
                logging.warning(f"Invalid or expired session token: {session_token}")
                return None
        except jwt.JWTError as e:
            logging.error(f"Error validating session token: {e}")
            return None

    def renew_session(self, session_token):
        if session_token in self.sessions:
            self.sessions[session_token]["expires"] = datetime.utcnow() + timedelta(minutes=30)
            return self.sessions[session_token]["user_id"]
        else:
            logging.warning(f"Session token not found: {session_token}")
            return None
