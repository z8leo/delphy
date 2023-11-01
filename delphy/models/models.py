from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from enum import Enum


class DocumentChunk(BaseModel):
    id: str = None
    parent_id: str = None
    content: str = None
    type: str = "chunk"

class DocumentMetaData(BaseModel):
    title: str = None
    type: str = "metadata"

class Document(BaseModel):
    id: str = None
    summary: str = "Document"
    children: Optional[List[DocumentChunk]] = None
    metadata: Optional[DocumentMetaData] = None
    type: str = "document"

    def add_child(self, child: DocumentChunk):
        child.parent_id = self.id  # set parent id when adding child
        self.children.append(child)