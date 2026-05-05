# Architecture

The Autonomous Research Agent is built on a multi-agent architecture designed for high throughput, scalability, and deep semantic understanding.

## Core Components

### 1. Multi-Agent System
- **Research Planner**: Responsible for task decomposition. It takes a broad research topic and breaks it down into structured, actionable queries.
- **Paper Analyzer**: Handles the heavy lifting of data ingestion. It interfaces with external APIs (arXiv), downloads papers, and extracts key entities and summaries.
- **Insight Generator**: The synthesis engine. It looks across multiple analyzed papers to identify correlations, contradictions, and future research directions.

### 2. Core Infrastructure
- **Persistent Memory (`core/memory.py`)**: Uses ChromaDB for vector-based semantic search. This allows the system to build longitudinal context across research sessions.
- **Context Manager (`core/context.py`)**: Ensures that token limits are strictly adhered to, maximizing the efficiency of the MiniMax M2.5 model via the Akash API.
- **Batch Processor (`core/batch.py`)**: Optimizes API calls and processing to handle 50+ papers daily asynchronously.
- **Tools (`core/tools.py`)**: Abstractions for external services like arXiv and Google Scholar.

## Data Flow

1. User provides a topic to the CLI.
2. `ResearchPlanner` queries the `PersistentMemory` for historical context, then generates a JSON-structured plan.
3. `PaperAnalyzer` receives the plan, fetches metadata via `ArxivTool`, and processes papers concurrently using `BatchProcessor`.
4. `ContextManager` ensures summaries and extracted text fit within the prompt window.
5. `InsightGenerator` pulls all summaries, compares them, and generates the final output.
6. All intermediate and final results are stored in `PersistentMemory`.