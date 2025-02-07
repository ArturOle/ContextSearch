from keybert import KeyBERT
from typing import List, Tuple

from ..data_classes import Tag, RelationWeight, Chunk


class Extractor:
    def __init__(self):
        self.kw_model = KeyBERT()

    def extract_keywords(self, text_list: List[str]) -> list:
        joined_text = ''.join(text_list)
        keywords = self.kw_model.extract_keywords(
            joined_text,
            keyphrase_ngram_range=(1, 1),
            top_n=10,
            word_embeddings=self.kw_model.extract_embeddings(joined_text)[1]
        )

        return keywords

    def produce_tags_and_relations(
            self,
            chunks: List[Chunk],
            filename: str
    ) -> Tuple[List[Tag], List[RelationWeight]]:
        tags = {}
        for chunk in chunks:
            ranked_phrases = self.extract_keywords(chunk.text)

            tags = {
                tag[0]: tag[1] for tag in ranked_phrases
                if tags.get(tag[0], 0) <= tag[1]
            }

        tag_dtos = []
        relations = []
        for tag in tags.items():
            tag_dto = Tag(
                text=tag[0]
            )
            tag_dtos.append(tag_dto)

            relations.append(
                RelationWeight(
                    literature=filename,
                    tag=tag_dto.text,
                    weight=tag[1]
                )
            )

        return tag_dtos, relations
