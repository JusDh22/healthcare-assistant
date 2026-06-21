from typing import Dict, List, Any
import json
from src.utils.logger import logger

class AgentPlanner:
    """Plans and decomposes complex medical queries into sub-tasks"""
    
    AVAILABLE_TOOLS = {
        "appointment_booking": "Book medical appointments with doctors",
        "medical_records_retrieval": "Retrieve and manage patient medical records",
        "disease_search": "Search for disease information from medical databases",
        "patient_summary": "Generate patient medical summary",
        "appointment_tracking": "Track appointment status"
    }
    
    def __init__(self):
        pass
    
    def decompose_query(self, user_query: str, patient_context: str = "") -> Dict[str, Any]:
        """
        Decompose user query into structured plan
        
        Args:
            user_query: The patient's or attendant's query
            patient_context: Existing patient context
        
        Returns:
            Dictionary containing goals, subtasks, and execution plan
        """
        try:
            plan = self._simple_plan(user_query, patient_context)
            logger.info(f"Query decomposed successfully: {plan}")
            return plan
        except Exception as e:
            logger.error(f"Error decomposing query: {e}")
            raise
    
    def _simple_plan(self, user_query: str, patient_context: str) -> Dict[str, Any]:
        """
        Create a simple plan based on query keywords
        """
        query_lower = user_query.lower()
        
        plan = {
            "goals": [],
            "subtasks": [],
            "tools_needed": [],
            "execution_order": []
        }
        
        # Detect intent
        if "book" in query_lower or "appointment" in query_lower:
            plan["goals"].append("Book medical appointment")
            plan["subtasks"].append("Find available doctor slots")
            plan["subtasks"].append("Book appointment with selected doctor")
            plan["tools_needed"].append("appointment_booking")
            plan["tools_needed"].append("appointment_booking")
        
        if "medical" in query_lower and "record" in query_lower:
            plan["goals"].append("Retrieve medical records")
            plan["subtasks"].append("Fetch patient medical history")
            plan["tools_needed"].append("medical_records_retrieval")
        
        if "disease" in query_lower or "treatment" in query_lower or "condition" in query_lower:
            plan["goals"].append("Search medical information")
            plan["subtasks"].append("Search for disease/condition information")
            plan["tools_needed"].append("disease_search")
        
        if "summary" in query_lower or "summarize" in query_lower:
            plan["goals"].append("Summarize patient information")
            plan["subtasks"].append("Generate patient summary")
            plan["tools_needed"].append("patient_summary")
        
        return plan
    
    def validate_plan(self, plan: Dict[str, Any]) -> bool:
        """Validate if plan is executable"""
        try:
            required_fields = ["goals", "subtasks", "tools_needed"]
            for field in required_fields:
                if field not in plan or not plan[field]:
                    logger.warning(f"Missing field in plan: {field}")
                    return False
            
            for tool in plan.get("tools_needed", []):
                if tool not in self.AVAILABLE_TOOLS:
                    logger.warning(f"Unknown tool requested: {tool}")
                    return False
            
            return True
        except Exception as e:
            logger.error(f"Error validating plan: {e}")
            return False
