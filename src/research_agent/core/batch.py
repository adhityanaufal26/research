from typing import List, Any, Callable
import concurrent.futures
import logging

logger = logging.getLogger(__name__)

class BatchProcessor:
    """
    Batch processing optimization to handle 50+ papers daily efficiently.
    """
    
    def __init__(self, max_workers: int = 4):
        self.max_workers = max_workers
        
    def process(self, items: List[Any], process_func: Callable[[Any], Any]) -> List[Any]:
        """
        Processes items in parallel batches.
        """
        results = []
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            future_to_item = {executor.submit(process_func, item): item for item in items}
            
            for future in concurrent.futures.as_completed(future_to_item):
                item = future_to_item[future]
                try:
                    data = future.result()
                    results.append(data)
                except Exception as exc:
                    logger.error(f'Item generated an exception: {exc}')
                    
        return results