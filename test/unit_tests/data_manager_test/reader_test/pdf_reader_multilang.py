import os
import logging

from context_search.reader import PDFReader

cur_dir = os.path.dirname(__file__)
logger = logging.getLogger(__name__)


def test_lang_detect_pl(mocker):
    pdf_reader = PDFReader()
    with mocker.patch.object(
        pdf_reader,
        "_detect_lang",
        wraps=pdf_reader._detect_lang
    ) as detect_lang_mock:
        pdf_reader.read(
            rf'{cur_dir}/test_files/test_pl.pdf'
        )
        assert detect_lang_mock.return_value == "pol"


def test_lang_detect_en(mocker):
    pdf_reader = PDFReader()
    with mocker.patch.object(
        pdf_reader,
        "_detect_lang",
        wraps=pdf_reader._detect_lang
    ) as detect_lang_mock:
        pdf_reader.read(
            rf'{cur_dir}/test_files/test_eng.pdf'
        )
        assert detect_lang_mock.return_value == "eng"


def test_lang_detect_not_supported(mocker):
    pdf_reader = PDFReader()
    with mocker.patch.object(
        pdf_reader,
        "_detect_lang",
        wraps=pdf_reader._detect_lang
    ) as detect_lang_mock:
        pdf_reader.read(
            rf'{cur_dir}/test_files/test_kor.pdf'
        )
        assert detect_lang_mock.return_value == "eng"
