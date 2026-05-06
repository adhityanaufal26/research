from typing import Dict, Any, List
import logging
from research_agent.core.tools import ArxivTool
from research_agent.core.batch import BatchProcessor

logger = logging.getLogger(__name__)


class PaperAnalyzer:
    """
    Fetches papers, extracts entities, and summarizes findings.
    """

    def __init__(self, memory: Any, context_mgr: Any):
        self.memory = memory
        self.context_mgr = context_mgr
        self.arxiv_tool = ArxivTool()
        self.batch_processor = BatchProcessor()

    def execute_plan(self, plan: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Executes the research plan by fetching and analyzing papers.
        """
        queries = plan.get("queries", [])
        target_count = plan.get("target_paper_count", 5)

        all_papers = []
        for query in queries:
            logger.info(f"Fetching papers for query: {query}")
            papers = self.arxiv_tool.search(
                query, max_results=target_count // len(queries) + 1
            )
            all_papers.extend(papers)

        # Deduplicate
        unique_papers = {p["id"]: p for p in all_papers}.values()

        # Batch process for entity extraction and summarization
        logger.info(f"Processing {len(unique_papers)} papers in batches...")

        def process_paper(paper):
            # Simulate token-efficient processing using MiniMax M2.5
            summary = f"Summary of {paper['title']} focusing on key findings."
            entities = ["Entity1", "Entity2", "Methodology"]
            return {
                "id": paper["id"],
                "title": paper["title"],
                "summary": summary,
                "entities": entities,
                "authors": paper["authors"],
            }

        results = self.batch_processor.process(list(unique_papers), process_paper)

        # Store results in memory
        for res in results:
            self.memory.store(
                document=res["summary"],
                metadata={
                    "type": "paper_analysis",
                    "paper_id": res["id"],
                    "title": res["title"],
                },
            )

        return results
