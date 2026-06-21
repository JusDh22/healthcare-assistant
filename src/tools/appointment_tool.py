from typing import Dict, Any
from src.utils.logger import logger

class AppointmentTool:
    """Tool for managing medical appointments"""
    
    def __init__(self):
        pass
    
    def execute(self, task: str) -> Dict[str, Any]:
        """Execute appointment-related task"""
        if "book" in task.lower():
            return self.book_appointment(task)
        elif "available" in task.lower():
            return self.get_available_slots(task)
        elif "cancel" in task.lower():
            return self.cancel_appointment(task)
        else:
            return {"error": "Unknown appointment task"}
    
    def book_appointment(self, task: str) -> Dict[str, Any]:
        """Book an appointment"""
        try:
            logger.info(f"Booking appointment: {task}")
            return {
                "success": True,
                "appointment_id": "APT001",
                "status": "booked",
                "message": "Appointment successfully booked"
            }
        except Exception as e:
            logger.error(f"Error booking appointment: {e}")
            return {"error": str(e)}
    
    def get_available_slots(self, task: str) -> Dict[str, Any]:
        """Get available appointment slots"""
        try:
            logger.info(f"Retrieving available slots: {task}")
            return {
                "success": True,
                "available_slots": [
                    {"id": 1, "date": "2024-01-15", "time": "10:00 AM"},
                    {"id": 2, "date": "2024-01-16", "time": "2:00 PM"}
                ],
                "count": 2
            }
        except Exception as e:
            logger.error(f"Error getting slots: {e}")
            return {"error": str(e)}
    
    def cancel_appointment(self, task: str) -> Dict[str, Any]:
        """Cancel an appointment"""
        try:
            logger.info(f"Cancelling appointment: {task}")
            return {
                "success": True,
                "appointment_id": "APT001",
                "status": "cancelled"
            }
        except Exception as e:
            logger.error(f"Error cancelling appointment: {e}")
            return {"error": str(e)}
