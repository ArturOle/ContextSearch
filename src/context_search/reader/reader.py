
import os
import logging
import fitz
import pytesseract

from abc import ABC, abstractmethod
from fast_langdetect import detect
from pdf2image import convert_from_path
from typing import List

from ..data_classes import LiteratureDTO
from ..utils import setup_logger, EnvInterface

current_directory = os.path.dirname(__file__)
logger = setup_logger('Reader Logger', 'logs.log', logging.INFO)
SUPPORTED_LENGUAGES = {
    "pl": "pol",
    "en": "eng",
}


class ReadManager:
    _readers = {}

    @property
    def pdf_reader(self):
        reader = self._readers.get("pdf", None)
        if reader is None:
            self._readers["pdf"] = PDFReader()
            return self._readers["pdf"]
        return reader

    @property
    def text_reader(self):
        reader = self._readers.get("txt", None)
        if reader is None:
            self._readers["txt"] = TextReader()
            return self._readers["txt"]
        return reader

    @property
    def docx_reader(self):
        reader = self._readers.get("docx", None)
        if reader is None:
            self._readers["docx"] = DocxReader()
            return self._readers["docx"]
        return reader

    @staticmethod
    def _is_path_valid(data_path: str) -> bool:
        return os.path.exists(data_path)

    @staticmethod
    def _is_directory_or_file(data_path: str) -> bool:
        return FileTypeRecon.is_directory_or_file(data_path)

    # A depth first search may be beneficial here to search directory.
    # However, it may not be very safe... This should be disabled for web
    # service and secured for the desktop. Idea, after searching through files
    # give user possibility to disable files he wants to exclude.
    def read(self, data_path: str) -> List[LiteratureDTO]:
        if self._is_directory_or_file(data_path):
            return self._read_directory(data_path)
        else:
            return [self._read_file(data_path)]

    def _read_directory(self, directory_path: str) -> List[LiteratureDTO]:
        return [
            self._read_file(os.path.join(directory_path, file_name))
            for file_name in os.listdir(directory_path)
        ]

    def _read_file(self, file_path: str) -> LiteratureDTO:
        file_type = FileTypeRecon.recognize_type(file_path)
        text = None

        match file_type:
            case 'pdf':
                text = self.pdf_reader.read(file_path)
            case 'txt':
                text = self.text_reader.read(file_path)

        return LiteratureDTO(
            filename=os.path.basename(file_path),
            filepath=file_path,
            text=text
        )


class AbstractReader(ABC):

    @abstractmethod
    def read(self, data_path: str) -> List[str]:
        pass


class TextReader(AbstractReader):

    @staticmethod
    def read(data_path: str) -> List[str]:
        with open(data_path, 'r') as file:
            return [file.read()]


class PDFReader(AbstractReader):
    """
    PDFReader class handles the reading of both difital and scanned PDF files
    with PyMuPDF and pytesseract libraries. If the document is scanned, the
    text is extracted using OCR.
    """
    def __init__(self):
        self.tesseract_path = ""
        self.poppler_path = ""
        self._setup_paths_from_config()

    def _setup_paths_from_config(self):
        """
        Assures that if the paths are not set in the environment variables,
        they are set from the config file. After sercond iteration it
        should not be necessary, as the paths should be set in the
        environment variables.

        To work properly, the config.ini file should be in the same
        directory as the script that is being run with paths to tesseract
        and poppler bin folder (NOT TO EXECUTABLES, BUT FOLDERS).
        """
        self.tesseract_path = os.getenv("TESSERACT_PATH")
        self.poppler_path = os.getenv("POPPLER_PATH")

        if not self.tesseract_path or not self.poppler_path:
            ocr_vars = EnvInterface.get_OCR_vars()
            self.tesseract_path = ocr_vars.get("TESSERACT_PATH")
            self.poppler_path = ocr_vars.get("POPPLER_PATH")

        if os.name == "nt":
            # system specific path for windows
            pytesseract.pytesseract.tesseract_cmd = os.path.join(
                self.tesseract_path, "tesseract.exe"
            )
        else:
            # system specific path for linux
            pytesseract.pytesseract.tesseract_cmd = self.tesseract_path

    def read(self, data_path: str) -> List[str]:
        doc = fitz.open(data_path)

        paged_text = []
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)
            page_text = page.get_text()
            paged_text.append(page_text)

        doc.close()

        if ''.join(paged_text) == "":
            logger.info(
                'No text found in document which indicates scan, trying OCR'
            )
            paged_text = self._read_file_ocr(data_path)

        return paged_text

    @staticmethod
    def _detect_lang(string):
        string = string.replace("\n", ' ')
        lang = detect(string)["lang"]
        return SUPPORTED_LENGUAGES.get(lang, "eng")

    def _read_file_ocr(self, file_path):

        pages = convert_from_path(file_path, 300)

        # we sacrifice one execution of tesseract to
        # to detect main lenguage of analyzed text
        lang = self._detect_lang(pytesseract.image_to_string(pages[0]))

        paged_text = []
        for page in pages:
            page_text = pytesseract.image_to_string(page, lang)
            paged_text.append(page_text)

        return paged_text


class DocxReader(AbstractReader):
    # To be implemented in future versions
    @staticmethod
    def read(data_path: str) -> List[str]:
        raise NotImplementedError


class FileTypeRecon:
    file_type_classes = {
        'txt',
        'pdf'
    }

    @staticmethod
    def is_path_valid(data_path: str) -> bool:
        return os.path.exists(data_path)

    @staticmethod
    def is_directory_or_file(data_path: str) -> bool:
        if os.path.isdir(data_path):
            return True
        elif os.path.isfile(data_path):
            return False

    @staticmethod
    def recognize_type(data_path):
        for file_type in FileTypeRecon.file_type_classes:
            if data_path.endswith(file_type):
                return file_type
        else:
            filename = os.path.basename(data_path)
            logger.warning(
                f'Unsupported file type. The file {filename} will be skipped.'
                "Please provide a file of the following types: "
                ", ".join(FileTypeRecon.file_type_classes)
            )
