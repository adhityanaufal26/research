import pytest
from research_agent.agents.planner import ResearchPlanner
from research_agent.core.memory import PersistentMemory

def test_planner_creates_plan():
    memory = PersistentMemory(collection_name="test_memory", persist_directory="./.test_db")
    planner = ResearchPlanner(memory=memory)
    
    plan = planner.create_plan(topic="Quantum Computing", paper_count=5)
    
    assert plan["topic"] == "Quantum Computing"
    assert plan["target_paper_count"] == 5
    assert len(plan["queries"]) > 0
    assert "steps" in plan