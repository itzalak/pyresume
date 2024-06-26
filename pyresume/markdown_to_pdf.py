import os
import sys

from md2pdf.core import md2pdf

from default_resume import DefaultResume
from file_actions import FileActions


def generate_pdf(style: str, markdown_file: str):
    """Generate pdf file using a given style based of a markdown file"""

    if markdown_file is DefaultResume.default_resume_path:
        output_pdf_path = DefaultResume.resume_path()
    else:
        output_pdf_path = FileActions.build_output_path(markdown_file)

    md2pdf(output_pdf_path, md_file_path=markdown_file, css_file_path=style)

    FileActions.validate_file_exists(output_pdf_path)
    print(f"File created successfully with name: {os.path.basename(output_pdf_path)}")


def main(style: str, markdown_file: str):
    try:
        FileActions.validate_file_exists(style)
        FileActions.validate_file_exists(markdown_file)
        generate_pdf(style, markdown_file)
    except (FileNotFoundError, ValueError) as err:
        print(f"Fatal error: {err}")
        print("Application was terminated gracefully...")
        sys.exit(1)
