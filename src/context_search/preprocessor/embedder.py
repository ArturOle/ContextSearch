
from fastembed import TextEmbedding
from typing import List

from ..data_classes import Embeddable


class AbstractEmbedder:
    def embed(self, text):
        raise NotImplementedError

    def produce_embeddings(
            self,
            embeddable_objs: List[Embeddable]
    ) -> List[Embeddable]:
        raise NotImplementedError


class ImageEmbedder(AbstractEmbedder):
    def embed(self, text):
        raise NotImplementedError

    def produce_embeddings(
            self,
            embeddable_objs: List[Embeddable]
    ) -> List[Embeddable]:
        raise NotImplementedError


class TextEmbedder:
    def __init__(self, model_id="intfloat/e5-base-v2"):
        self.model = TextEmbedding(
            model_name=model_id
        )

    def embed(self, text):
        """Embeds the given text using the model."""
        return self.model.embed(text)

    def __call__(self, doc):
        doc._.embedding = self.embed(doc.text)
        return doc

    def produce_embeddings(
            self,
            embeddable_objs: List[Embeddable]
    ) -> List[Embeddable]:
        """Produces embeddings for the given list of Embeddable objects."""

        for embeddable_obj in embeddable_objs:
            embeddable_obj.embeddings = self.embed(
                embeddable_obj.text
            )

        return embeddable_objs
