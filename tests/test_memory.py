import pytest
import shutil
import os
from research_agent.core.memory import PersistentMemory

@pytest.fixture
def memory():
    test_dir = "./.test_chroma_db"
    mem = PersistentMemory(collection_name="test_collection", persist_directory=test_dir)
    yield mem
    # Cleanup
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)

def test_memory_store_and_search(memory):
    doc_id = memory.store(
        document="Large Language Models are scaling rapidly.",
        metadata={"topic": "LLM"}
    )
    
    assert doc_id is not None
    
    results = memory.search("scaling language models")
    
    assert len(results) > 0
    assert "Large Language" in results[0]["document"]