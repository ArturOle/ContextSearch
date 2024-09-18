import torch
from transformers import AutoModel, AutoTokenizer
from typing import List

from ..data_classes import Embeddable


class Embedder:
    def __init__(self, model_id="intfloat/e5-base-v2"):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tokenizer = AutoTokenizer.from_pretrained(model_id)
        self.model = AutoModel.from_pretrained(model_id).to(self.device)
        self.model.eval()

    def embed(self, text):
        with torch.no_grad():
            inputs = self.tokenizer(
                text,
                return_tensors="pt",
                padding=True,
                truncation=True
            ).to(self.device)
            outputs = self.model(**inputs)
            squeezed_output = outputs.last_hidden_state.mean(dim=1).squeeze()
            return squeezed_output.cpu().numpy()

    def __call__(self, doc):
        doc._.embedding = self.embed(doc.text)
        return doc

    def produce_embeddings(
            self,
            embeddable_objs: List[Embeddable]
    ) -> List[Embeddable]:

        for embeddable_obj in embeddable_objs:
            embeddable_obj.embeddings = self.embed(
                embeddable_obj.text
            )

        return embeddable_objs
