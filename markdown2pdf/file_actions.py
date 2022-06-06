import glob
import os
import pathlib

from settings import OUTPUT_DIR, MODULE_DIR


class FileActions:

    @staticmethod
    def locate_directory(path) -> bool:
        """Check if the given path is a directory"""
        return os.path.isdir(path)

    @staticmethod
    def validate_file_exists(path):
        """Check if the given path is a file, if not raise an exception"""
        if not os.path.isfile(path):
            raise FileNotFoundError(f'No file was found on path: {path}')

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
        """Build new filename for pdf file"""
        filename = os.path.basename(path)
        pdf_filename = cls.replace_extensions_markdown_for_pdf(filename)
        return os.path.join(OUTPUT_DIR, pdf_filename)

    @staticmethod
    def remove_pdf_files_from_output_dir():
        """Remove PDF files from output dir if some exist"""
        output_pdfs = glob.glob(f'{MODULE_DIR}/../output/*.pdf')
        if output_pdfs:
            for pdf in output_pdfs:
                os.remove(pdf)
