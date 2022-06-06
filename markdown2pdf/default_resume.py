import datetime
import os

from settings import OUTPUT_DIR, ASSETS_DIR


class DefaultResume:
    default_resume_path = os.path.join(ASSETS_DIR, "resume.md")

    @staticmethod
    def build_output_resume_filename():
        """Create pdf name with timestamp identifier"""
        timestamp = datetime.date.today()
        pdf_filename = f'resume-{timestamp}.pdf'
        return pdf_filename

    @classmethod
    def resume_path(cls):
        """Create resume output path"""
        pdf_filename = cls.build_output_resume_filename()
        return os.path.join(OUTPUT_DIR, pdf_filename)
