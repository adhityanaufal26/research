import gc
import pytest
import shutil
import os
import time
from research_agent.core.memory import PersistentMemory


def _rmtree_retry(path, retries=5, delay=0.5):
    """Remove directory tree with retry logic for Windows file locking issues."""
    for i in range(retries):
        try:
            shutil.rmtree(path, onexc=lambda *args: None)
            return
        except PermissionError:
            gc.collect()
            time.sleep(delay)
    # Final attempt - ignore all errors
    try:
        shutil.rmtree(path, onexc=lambda *args: None)
    except Exception:
        pass


@pytest.fixture
def memory():
    test_dir = "./.test_chroma_db"
    mem = PersistentMemory(
        collection_name="test_collection", persist_directory=test_dir
    )
    yield mem
    # Close the client to release file handles
    mem.close()
    # Force garbage collection to release any lingering references
    gc.collect()
    # Cleanup with retry
    if os.path.exists(test_dir):
        _rmtree_retry(test_dir)


def test_memory_store_and_search(memory):
    doc_id = memory.store(
        document="Large Language Models are scaling rapidly.", metadata={"topic": "LLM"}
    )

    assert doc_id is not None

    results = memory.search("scaling language models")

    assert len(results) > 0
    assert "Large Language" in results[0]["document"]
