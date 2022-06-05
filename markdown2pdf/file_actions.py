import datetime
import os

from settings import OUTPUT_DIR


class FileActions:

    @staticmethod
    def locate_directory(path):
        """Check if the given path is a directory"""
        return os.path.isdir(path)

    @staticmethod
    def locate_file(path):
        """Check if the given path is a file"""
        print(path)
        return os.path.isfile(path)

    @staticmethod
    def create_filename():
        """Create pdf name with timestamp identifier"""
        timestamp = datetime.date.today()
        pdf_filename = f"resume-{timestamp}.pdf"
        return pdf_filename

    @classmethod
    def resume_path(cls):
        """Create path from filename and output dir"""
        pdf_filename = cls.create_filename()
        return f"{OUTPUT_DIR}/{pdf_filename}"

    @staticmethod
    def file_path(name: str):
        clean_name = name.replace(".md", "")
        return f"{OUTPUT_DIR}/{clean_name}.pdf"
