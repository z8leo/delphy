import pytest
import delphy.datastore.providers.chromadb as chromadb
# import models
from delphy.models.models import Document, DocumentChunk, DocumentMetaData

class TestChromaDataStore:
    """Test the ChromaDB DataStore implementation."""

    @pytest.fixture(scope="session")
    def datastore(self):
        """Init a ChromaDB DataStore instance."""
        return chromadb.ChromaDataStore()

    # Fixture for test data
    @pytest.fixture(scope="session")
    def mock_data(self) -> Document:
        """Create a test data record."""
        return Document(
            id="test",
            children=[
                DocumentChunk(
                    id="child_test",
                    parent_id="test",
                    content="test"
                )
            ],
            metadata=DocumentMetaData(
                title="test"
            )
        )

    def test_init(self, datastore):
        """Test that the ChromaDB DataStore can be initialized."""
        assert datastore is not None

    def test_upsert(self, datastore, mock_data):
        """Test that the ChromaDB DataStore can upsert a a document."""
        datastore.upsert(mock_data)
        result = datastore.get_document(mock_data.id)
        assert result is not None
        assert result.id == mock_data.id