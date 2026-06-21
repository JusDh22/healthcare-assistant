import pytest
from src.agents.planner import AgentPlanner
from src.agents.executor import AgentExecutor
from src.agents.memory_manager import MemoryManager


class TestAgentPlanner:
    def test_decompose_appointment_query(self):
        planner = AgentPlanner()
        query = "Book an appointment with a nephrologist"
        plan = planner.decompose_query(query)
        
        assert plan["goals"]
        assert plan["subtasks"]
        assert plan["tools_needed"]
    
    def test_validate_plan(self):
        planner = AgentPlanner()
        query = "Book an appointment"
        plan = planner.decompose_query(query)
        
        assert planner.validate_plan(plan)


class TestAgentExecutor:
    def test_execute_plan(self):
        executor = AgentExecutor()
        memory_manager = MemoryManager()
        session_id = memory_manager.create_session()
        
        query = "Book an appointment with a doctor"
        result = executor.execute_plan(query, session_id)
        
        assert result["success"]
        assert result["session_id"] == session_id


class TestMemoryManager:
    def test_create_session(self):
        manager = MemoryManager()
        session_id = manager.create_session()
        
        assert session_id
        assert len(session_id) > 0
    
    def test_store_and_retrieve_context(self):
        manager = MemoryManager()
        session_id = manager.create_session()
        
        manager.store_context(session_id, "test_key", "test_value")
        value = manager.retrieve_context(session_id, "test_key")
        
        assert value == "test_value"
