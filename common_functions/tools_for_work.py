import configparser
import os

class LinkPreparer:
    @staticmethod
    def prepare_link(link: str) -> str:
        """Adds 'http://' to the link if it is missing."""
        if not link.startswith('http://'):
            return f'http://{link}'
        return link

class FileOperations:
    @staticmethod
    def is_directory_exists(directory_path: str) -> bool:
        """Checks if the directory exists."""
        return os.path.isdir(directory_path)

    @staticmethod
    def is_file_exists(file_path: str) -> bool:
        """Checks if the file exists."""
        return os.path.isfile(file_path)

class ConfigFile:
    def __init__(self):
        self.config = configparser.ConfigParser()

    def read_config(self, path: str) -> configparser.ConfigParser:
        """Reads the configuration file and returns the config object."""
        self.config.read(path)
        return self.config
