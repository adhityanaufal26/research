import argparse
import logging
from dotenv import load_dotenv

from research_agent.agents.planner import ResearchPlanner
from research_agent.agents.analyzer import PaperAnalyzer
from research_agent.agents.generator import InsightGenerator
from research_agent.core.context import ContextManager
from research_agent.core.memory import PersistentMemory

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description="Autonomous Research Agent")
    parser.add_argument(
        "--topic", type=str, required=True, help="Research topic to analyze"
    )
    parser.add_argument(
        "--papers", type=int, default=5, help="Number of papers to fetch and analyze"
    )
    args = parser.parse_args()

    load_dotenv()
    logger.info(f"Starting research on topic: {args.topic}")

    # Initialize core modules
    memory = PersistentMemory(collection_name="research_memory")
    context_mgr = ContextManager()

    # Initialize agents
    planner = ResearchPlanner(memory=memory)
    analyzer = PaperAnalyzer(memory=memory, context_mgr=context_mgr)
    generator = InsightGenerator(memory=memory)

    try:
        # Phase 1: Planning
        logger.info("Phase 1: Generating research plan")
        plan = planner.create_plan(topic=args.topic, paper_count=args.papers)

        # Phase 2: Analysis
        logger.info("Phase 2: Fetching and analyzing papers")
        analysis_results = analyzer.execute_plan(plan)

        # Phase 3: Insights Generation
        logger.info("Phase 3: Generating insights and correlations")
        insights = generator.generate_insights(analysis_results, topic=args.topic)

        # Output results
        print("\n" + "=" * 50)
        print("RESEARCH SUMMARY")
        print("=" * 50)
        print(f"Topic: {args.topic}")
        print(f"Papers Analyzed: {len(analysis_results)}")
        print("\nKey Insights:")
        print(insights.get("summary", "No summary generated."))

        print("\nFuture Directions:")
        for direction in insights.get("future_directions", []):
            print(f"- {direction}")

    except Exception as e:
        logger.error(f"Research pipeline failed: {str(e)}")


if __name__ == "__main__":
    main()
