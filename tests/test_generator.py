import pytest
from research_agent.agents.generator import InsightGenerator

class MockMemory:
    def store(self, *args, **kwargs):
        pass
        
    def search(self, *args, **kwargs):
        return []

def test_generator_creates_insights():
    generator = InsightGenerator(memory=MockMemory())
    
    papers = [
        {"id": "1", "title": "Paper 1", "summary": "Sum 1"},
        {"id": "2", "title": "Paper 2", "summary": "Sum 2"}
    ]
    
    insights = generator.generate_insights(papers, topic="AI")
    
    assert "topic" in insights
    assert "summary" in insights
    assert "trends" in insights
    assert "future_directions" in insights