import chromadb
from typing import List, Dict, Any
import uuid


class PersistentMemory:
    """
    Persistent memory with semantic search for longitudinal research.
    Utilizes ChromaDB for vector storage.
    """

    def __init__(
        self,
        collection_name: str = "research_memory",
        persist_directory: str = "./.chroma_db",
    ):
        self.client = chromadb.PersistentClient(path=persist_directory)
        self.collection = self.client.get_or_create_collection(name=collection_name)

    def store(
        self, document: str, metadata: Dict[str, Any] = None, doc_id: str = None
    ) -> str:
        """
        Stores a document in the semantic database.
        """
        if doc_id is None:
            doc_id = str(uuid.uuid4())

        self.collection.add(
            documents=[document],
            metadatas=[metadata] if metadata else [{}],
            ids=[doc_id],
        )
        return doc_id

    def close(self):
        """
        Closes the ChromaDB client to release file handles.
        Important for cleanup on Windows.
        """
        self.collection = None
        self.client = None

    def search(self, query: str, n_results: int = 5) -> List[Dict[str, Any]]:
        """
        Semantic search for longitudinal research correlation.
        """
        if self.collection.count() == 0:
            return []

        results = self.collection.query(
            query_texts=[query], n_results=min(n_results, self.collection.count())
        )

        formatted_results = []
        if results["documents"] and results["documents"][0]:
            for i in range(len(results["documents"][0])):
                formatted_results.append(
                    {
                        "document": results["documents"][0][i],
                        "metadata": (
                            results["metadatas"][0][i] if results["metadatas"] else {}
                        ),
                        "id": results["ids"][0][i],
                    }
                )

        return formatted_results
