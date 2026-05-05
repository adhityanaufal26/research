from research_agent.agents.planner import ResearchPlanner
from research_agent.agents.analyzer import PaperAnalyzer
from research_agent.agents.generator import InsightGenerator
from research_agent.core.context import ContextManager
from research_agent.core.memory import PersistentMemory

def run_example():
    topic = "Autonomous Agents in Software Engineering"
    print(f"Starting research pipeline for: {topic}\n")
    
    # Init
    memory = PersistentMemory(collection_name="example_memory")
    context_mgr = ContextManager()
    
    planner = ResearchPlanner(memory=memory)
    analyzer = PaperAnalyzer(memory=memory, context_mgr=context_mgr)
    generator = InsightGenerator(memory=memory)
    
    # 1. Plan
    print("1. Creating Plan...")
    plan = planner.create_plan(topic, paper_count=3)
    print(f"Generated queries: {plan['queries']}\n")
    
    # 2. Analyze
    print("2. Analyzing Papers...")
    results = analyzer.execute_plan(plan)
    print(f"Analyzed {len(results)} papers.\n")
    
    # 3. Generate Insights
    print("3. Generating Insights...")
    insights = generator.generate_insights(results, topic)
    print("\nFinal Insights Summary:")
    print(insights["summary"])
    
if __name__ == "__main__":
    run_example()