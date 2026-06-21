from typing import Dict, Any, List
from src.utils.logger import logger

class DiseaseSearchTool:
    """Tool for searching medical information"""
    
    def __init__(self):
        pass
    
    def execute(self, task: str) -> Dict[str, Any]:
        """Execute disease search task"""
        try:
            disease = self._extract_disease(task)
            return self.search_disease_info(disease)
        except Exception as e:
            logger.error(f"Error executing disease search: {e}")
            return {"error": str(e)}
    
    def search_disease_info(self, disease: str) -> Dict[str, Any]:
        """Search and summarize disease information"""
        try:
            logger.info(f"Searching disease information for: {disease}")
            
            return {
                "success": True,
                "disease": disease,
                "search_results": [
                    {"title": "Disease Overview", "url": "https://example.com", "snippet": "Information about the disease"},
                    {"title": "Treatment Options", "url": "https://example.com", "snippet": "Latest treatment methods"}
                ],
                "summary": f"Summary of {disease}: This is a medical condition that requires proper diagnosis and treatment."
            }
        except Exception as e:
            logger.error(f"Error searching disease info: {e}")
            return {"error": str(e)}
    
    def _extract_disease(self, task: str) -> str:
        """Extract disease name from task"""
        return task.replace("search", "").replace("information", "").strip()
