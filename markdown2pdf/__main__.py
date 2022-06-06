import argparse
import sys

from css_styles import CssStyles
from default_resume import DefaultResume
from file_actions import FileActions
from markdown_to_pdf import main
from settings import __version__


def get_args():
    """Get application arguments"""
    args = argparse.ArgumentParser(description='Generate a pdf resume from a markdown file')
    group = args.add_mutually_exclusive_group()
    group.add_argument('-c', '--css', type=str, metavar='path/to/file.css', help='Path for the css style file.')
    group.add_argument('-simple', action='store_true', help='Generate pdf with simple style.')
    group.add_argument('-bar', action='store_true', help='Generate pdf with colored bar before headers.')
    group.add_argument('-divider', action='store_true', help='Generate pdf with colored divider between headers.')
    args.add_argument('-m', '--md', type=str, metavar='path/to/markdown/file.md', help='Path to input markdown file.')
    group.add_argument('-l', '--list', action='store_true', help='List all available styles.')
    group.add_argument('-r', '--remove', action='store_true', help='Remove all pdf files from output.')
    group.add_argument('-v', '--version', action='store_true', help='Print \'markdown2pdf\' version.')

    return args


def parse_final_args(parser: argparse.ArgumentParser):
    """Process final arguments"""
    args = parser.parse_args()

    if args.version:
        parser.exit(0, f'markdown2pdf {__version__}\n')

    if args.list:
        parser.exit(0, CssStyles.print_styles())

    if args.remove:
        FileActions.remove_pdf_files_from_output_dir()
        parser.exit(0, 'All files removed from output directory\n')


def parse_args(parser: argparse.ArgumentParser):
    """Process arguments"""
    args = parser.parse_args()
    markdown_file = DefaultResume.default_resume_path
    css_style = CssStyles.default_style

    if len(sys.argv) <= 1:
        print(f'No arguments given, defaulting to simple style')

    if args.md:
        markdown_file = args.md

    if args.bar:
        css_style = CssStyles.bar_style

    if args.divider:
        css_style = CssStyles.divider_style

    if args.simple:
        css_style = CssStyles.simple_style

    if args.css:
        css_style = args.css

    main(css_style, markdown_file)


if __name__ == '__main__':
    argparser = get_args()
    parse_final_args(argparser)
    parse_args(argparser)
