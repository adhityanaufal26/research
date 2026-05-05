import tiktoken

class ContextManager:
    """
    Token-efficient processing with dynamic context management.
    """
    
    def __init__(self, model_name: str = "gpt-3.5-turbo", max_tokens: int = 4000):
        # We use tiktoken as a fallback tokenizer representation
        try:
            self.encoding = tiktoken.encoding_for_model(model_name)
        except KeyError:
            self.encoding = tiktoken.get_encoding("cl100k_base")
            
        self.max_tokens = max_tokens
        
    def count_tokens(self, text: str) -> int:
        """
        Counts the number of tokens in a text.
        """
        return len(self.encoding.encode(text))
        
    def truncate_text(self, text: str, limit: int = None) -> str:
        """
        Truncates text to fit within token limits.
        """
        target_limit = limit or self.max_tokens
        tokens = self.encoding.encode(text)
        
        if len(tokens) <= target_limit:
            return text
            
        return self.encoding.decode(tokens[:target_limit])
        
    def build_context_window(self, priority_texts: list[str]) -> str:
        """
        Dynamically builds a context window from priority texts,
        ensuring it stays within token limits.
        """
        current_tokens = 0
        accepted_texts = []
        
        for text in priority_texts:
            tokens = self.count_tokens(text)
            if current_tokens + tokens < self.max_tokens:
                accepted_texts.append(text)
                current_tokens += tokens
            else:
                # Add partial text if we have space
                remaining_tokens = self.max_tokens - current_tokens
                if remaining_tokens > 50:
                    accepted_texts.append(self.truncate_text(text, remaining_tokens))
                break
                
        return "\n\n".join(accepted_texts)