from context_search.preprocessor.embedder import TextEmbedder
import pytest
import numpy as np
import random


random.seed(0)
np.random.seed(0)

text_to_embed = "This is a test text. This is a test text. This is a test text."


def test_creating_embeddings_from_text():
    embedder = TextEmbedder()
    embedding = embedder.embed(text_to_embed)

    assert pytest.approx(embedding, 1e-3) == np.load(
        "test/unit_tests/data_manager_test/preprocessor_test/test_embedding.npy"
    )
