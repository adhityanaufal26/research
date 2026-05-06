import pytest
from research_agent.agents.analyzer import PaperAnalyzer


class MockMemory:
    def store(self, *args, **kwargs):
        pass


class MockContext:
    pass


def test_analyzer_initialization():
    analyzer = PaperAnalyzer(memory=MockMemory(), context_mgr=MockContext())
    assert analyzer is not None
