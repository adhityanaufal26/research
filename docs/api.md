# API Reference

## `research_agent.agents`

### `ResearchPlanner`
- `create_plan(topic: str, paper_count: int = 10) -> Dict[str, Any]`
  Generates a structured research plan based on the input topic.

### `PaperAnalyzer`
- `execute_plan(plan: Dict[str, Any]) -> List[Dict[str, Any]]`
  Takes a research plan, fetches papers from arXiv, and extracts key entities.

### `InsightGenerator`
- `generate_insights(analyzed_papers: List[Dict], topic: str) -> Dict[str, Any]`
  Analyzes cross-paper correlations to output trends and future directions.

## `research_agent.core`

### `PersistentMemory`
- `store(document: str, metadata: Dict = None, doc_id: str = None) -> str`
  Stores text in the ChromaDB vector database.
- `search(query: str, n_results: int = 5) -> List[Dict]`
  Performs semantic search against the database.

### `ContextManager`
- `build_context_window(priority_texts: list[str]) -> str`
  Dynamically packs texts into a token-efficient string.

### `BatchProcessor`
- `process(items: List, process_func: Callable) -> List`
  Multithreaded execution for API calls and model inference.