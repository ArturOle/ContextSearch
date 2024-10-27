
from context_search.preprocessor import Preprocessor
from context_search.data_classes import LiteratureDTO
import numpy as np
import random
import pytest   # noqa: F401

random.seed(0)
np.random.seed(0)


def test_preprocessing_steps():
    pipeline = Preprocessor()
    texts = [LiteratureDTO(
        filename="name",
        filepath="path",
        text=["This is a test text"]
    )]

    literature = pipeline.process(texts)[0]
    assert literature.literature.filename == "name"
    assert literature.literature.filepath == "path"
    assert len(literature.chunks) == 1
    assert literature.chunks[0].text == "This is a test text"
    assert literature.chunks[0].page_number == 0


def test_multiple_file_processing():
    literatures = [
        LiteratureDTO(
            filename='test1.txt',
            filepath='test1.txt',
            text=['This is a test text']
        ),
        LiteratureDTO(
            filename='test2.txt',
            filepath='test2.txt',
            text=['This is a test text']
        ),
        LiteratureDTO(
            filename='test3.txt',
            filepath='test3.txt',
            text=['This is a test text']
        )
    ]
    processor_manager = Preprocessor()
    literatures = processor_manager.process(literatures)

    for i, literature in enumerate(literatures):
        assert literature.literature.filename == f'test{i + 1}.txt'
        assert literature.literature.filepath == f'test{i + 1}.txt'

    assert len(literatures) == 3
