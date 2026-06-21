from datetime import datetime
import json
from typing import Dict, Any, Optional
from src.utils.logger import logger
import uuid

class MemoryManager:
    def __init__(self):
        self.sessions = {}
    
    def create_session(self, patient_id: Optional[int] = None) -> str:
        """Create a new session for patient interaction"""
        session_id = str(uuid.uuid4())
        
        try:
            self.sessions[session_id] = {
                "patient_id": patient_id,
                "context": {},
                "memory_trace": [],
                "created_at": datetime.utcnow().isoformat()
            }
            
            logger.info(f"Created new session: {session_id}")
            return session_id
        except Exception as e:
            logger.error(f"Error creating session: {e}")
            raise
    
    def store_context(self, session_id: str, key: str, value: Any):
        """Store context in memory"""
        try:
            if session_id in self.sessions:
                self.sessions[session_id]["context"][key] = value
                logger.info(f"Stored context {key} for session {session_id}")
        except Exception as e:
            logger.error(f"Error storing context: {e}")
    
    def retrieve_context(self, session_id: str, key: Optional[str] = None) -> Any:
        """Retrieve context from memory"""
        try:
            if session_id in self.sessions:
                if key:
                    return self.sessions[session_id]["context"].get(key)
                else:
                    return self.sessions[session_id]["context"]
            return None
        except Exception as e:
            logger.error(f"Error retrieving context: {e}")
            return None
    
    def add_memory_trace(self, session_id: str, action: Dict[str, Any]):
        """Add action to memory trace"""
        try:
            if session_id in self.sessions:
                self.sessions[session_id]["memory_trace"].append({
                    "action": action,
                    "timestamp": datetime.utcnow().isoformat()
                })
                logger.info(f"Added memory trace for session {session_id}")
        except Exception as e:
            logger.error(f"Error adding memory trace: {e}")
    
    def get_memory_trace(self, session_id: str) -> list:
        """Get full memory trace for session"""
        try:
            if session_id in self.sessions:
                return self.sessions[session_id]["memory_trace"]
            return []
        except Exception as e:
            logger.error(f"Error retrieving memory trace: {e}")
            return []
    
    def clear_session(self, session_id: str):
        """Clear session memory"""
        try:
            if session_id in self.sessions:
                del self.sessions[session_id]
                logger.info(f"Cleared session: {session_id}")
        except Exception as e:
            logger.error(f"Error clearing session: {e}")
