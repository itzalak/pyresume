import os
import pathlib

from settings import OUTPUT_DIR


class FileActions:

    @staticmethod
    def locate_directory(path) -> bool:
        """Check if the given path is a directory"""
        return os.path.isdir(path)

    @staticmethod
    def locate_file(path) -> bool:
        """Check if the given path is a file"""
        print(path)
        return os.path.isfile(path)

    @staticmethod
    def replace_extensions_markdown_for_pdf(filename: str):
        """Replace markdown for pdf extension, if file extension is not markdown raise an error"""
        file_extension = pathlib.Path(filename).suffix
        if file_extension in ['.md', '.markdown']:
            return filename.replace(file_extension, '.pdf')
        else:
            raise ValueError(f'File must be from type markdown, instead {file_extension} was found')

    @classmethod
    def build_output_path(cls, path: str):
        filename = os.path.basename(path)
        pdf_filename = cls.replace_extensions_markdown_for_pdf(filename)
        return os.path.join(OUTPUT_DIR, pdf_filename)
