# ChromaDB Support

import chromadb
from delphy.models.models import Document

class ChromaDataStore():
    
    def __init__(self) -> None:
        self.client = chromadb.PersistentClient(path="./data/chromadb/chroma.db")
        self.collection = self.client.get_or_create_collection("delphy")

    def upsert(self, document: Document) -> None:
        """Upsert a document into the ChromaDB. Every Chunk is a separate document."""
        # Upsert document
        self.collection.upsert(ids=document.id, metadatas=document.metadata.model_dump(), documents=document.summary)
        # Upsert children
        for child in document.children:
            self.collection.upsert(ids=child.id, documents=child.content)

    def get_document(self, id: str) -> Document:
        """Get a document from the ChromaDB."""
        record = self.collection.get(ids=id)
        return Document(
            id=record["ids"][0],
            children=None,
            metadata=record["metadatas"][0],
        )