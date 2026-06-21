from typing import Dict, Any, Optional
import json
from src.agents.planner import AgentPlanner
from src.agents.memory_manager import MemoryManager
from src.utils.logger import logger
import time

class AgentExecutor:
    """Executes planned tasks sequentially"""
    
    def __init__(self):
        self.planner = AgentPlanner()
        self.memory_manager = MemoryManager()
    
    def execute_plan(self, user_query: str, session_id: str, patient_context: str = "") -> Dict[str, Any]:
        """
        Execute planned tasks
        
        Args:
            user_query: The original user query
            session_id: Session ID for memory tracking
            patient_context: Patient context information
        
        Returns:
            Execution results
        """
        try:
            # Create plan
            plan = self.planner.decompose_query(user_query, patient_context)
            
            if not self.planner.validate_plan(plan):
                return {"error": "Invalid plan", "details": plan}
            
            # Store plan in memory
            self.memory_manager.store_context(session_id, "plan", plan)
            
            # Execute subtasks
            results = {}
            for idx, subtask in enumerate(plan.get("subtasks", [])):
                logger.info(f"Executing subtask {idx + 1}: {subtask}")
                
                # Simulate tool execution
                try:
                    start_time = time.time()
                    result = {"status": "success", "data": f"Executed: {subtask}"}
                    execution_time = time.time() - start_time
                    
                    results[subtask] = result
                    
                    # Store in memory
                    self.memory_manager.add_memory_trace(session_id, {
                        "type": "task_execution",
                        "subtask": subtask,
                        "result": result,
                        "status": "success"
                    })
                except Exception as e:
                    logger.error(f"Error executing subtask {subtask}: {e}")
                    results[subtask] = {"error": str(e)}
            
            return {
                "success": True,
                "plan": plan,
                "results": results,
                "session_id": session_id
            }
        except Exception as e:
            logger.error(f"Error executing plan: {e}")
            return {"error": str(e), "success": False}
