"""
Tests for input validation in LEANN API.
"""

import pytest


def test_add_text_validates_type():
    """Test that add_text validates input type."""
    from leann.api import LeannBuilder

    builder = LeannBuilder(backend_name="hnsw")

    # Valid input should work
    builder.add_text("valid text")

    # Invalid inputs should raise TypeError
    with pytest.raises(TypeError, match="text must be a string"):
        builder.add_text(123)  # type: ignore

    with pytest.raises(TypeError, match="text must be a string"):
        builder.add_text(None)  # type: ignore

    with pytest.raises(TypeError, match="text must be a string"):
        builder.add_text(["list", "of", "strings"])  # type: ignore


def test_search_validates_query():
    """Test that search validates query input."""
    import tempfile
    from pathlib import Path

    from leann.api import LeannBuilder, LeannSearcher

    # Create a small index for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        index_path = str(Path(temp_dir) / "test.hnsw")

        builder = LeannBuilder(
            backend_name="hnsw",
            embedding_model="facebook/contriever",
            embedding_mode="sentence-transformers",
        )
        builder.add_text("test document")
        builder.build_index(index_path)

        searcher = LeannSearcher(index_path)

        # Valid query should work
        results = searcher.search("test", top_k=1)
        assert len(results) > 0

        # Invalid query type should raise TypeError
        with pytest.raises(TypeError, match="query must be a string"):
            searcher.search(123, top_k=1)  # type: ignore

        # Empty query should raise ValueError
        with pytest.raises(ValueError, match="query cannot be empty"):
            searcher.search("", top_k=1)

        # Whitespace-only query should raise ValueError
        with pytest.raises(ValueError, match="query cannot be empty"):
            searcher.search("   ", top_k=1)


def test_search_validates_top_k():
    """Test that search validates top_k parameter."""
    import tempfile
    from pathlib import Path

    from leann.api import LeannBuilder, LeannSearcher

    # Create a small index for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        index_path = str(Path(temp_dir) / "test.hnsw")

        builder = LeannBuilder(
            backend_name="hnsw",
            embedding_model="facebook/contriever",
            embedding_mode="sentence-transformers",
        )
        builder.add_text("test document")
        builder.build_index(index_path)

        searcher = LeannSearcher(index_path)

        # top_k < 1 should raise ValueError
        with pytest.raises(ValueError, match="top_k must be at least 1"):
            searcher.search("test", top_k=0)

        with pytest.raises(ValueError, match="top_k must be at least 1"):
            searcher.search("test", top_k=-1)
