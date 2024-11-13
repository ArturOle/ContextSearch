
import os
import tomllib
import logging


class EnvInterface:
    """
    Clas for managing shared values of config.toml
    After initizlization, the variables are shared across all instances
    on purpose so that it is accessible from different parts of
    system if needed.
    """
    _config = {}

    def __init__(self):
        current_working_directory = os.getcwd()
        path_to_config = os.path.join(
            current_working_directory,
            "config.toml"
        )
        self.read_config(path_to_config)

    def read_config(self, path):
        try:
            with open(path, "rb") as conf_file:
                EnvInterface._config = tomllib.load(conf_file)
        except FileNotFoundError as err:
            print(
                f"Could not find config file in the project root. {err}"
            )

    @staticmethod
    def get_OCR_vars():
        return EnvInterface._config.get("OCR")

    @staticmethod
    def get_neo4j_vars():
        return EnvInterface._config.get("neo4j")

    @staticmethod
    def set_env_variables_from_config():
        """
        Static method for setting env variables
        for necessary modules
        """
        for ocr_kwarg in EnvInterface.get_OCR_vars().items():
            os.environ[ocr_kwarg[0]] = ocr_kwarg[1]

        for db_kwarg in EnvInterface.get_neo4j_vars().items():
            os.environ[db_kwarg[0]] = db_kwarg[1]

