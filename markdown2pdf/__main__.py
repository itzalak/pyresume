import argparse
import sys

from file_utils import FileUtils
from markdown_to_pdf import generate_pdf
from settings import BAR_STYLE, SIMPLE_STYLE, DIVIDER_STYLE
from settings import __version__
from styles import print_styles


def get_args():
    """Get application arguments"""
    args = argparse.ArgumentParser(description='Generate a pdf resume from a markdown file')
    group = args.add_mutually_exclusive_group()
    group.add_argument('-s', '--style', type=str, metavar='path/to/file.css', help='Path for the css style file.')
    group.add_argument('-simple', action='store_true', help='Generate pdf with simple style.')
    group.add_argument('-bar', action='store_true', help='Generate pdf with colored bar before headers.')
    group.add_argument('-divider', action='store_true', help='Generate pdf with colored divider between headers.')
    args.add_argument("-l", '--list', action="store_true", help="List all available styles.")
    args.add_argument("-v", '--version', action="store_true", help="Print \"wal\" version.")

    return args


def parse_args(parser: argparse.ArgumentParser):
    """Process arguments"""
    args = parser.parse_args()
    if args.version:
        parser.exit(0, "markdown2pdf %s\n" % __version__)

    if args.list:
        print_styles()

    if len(sys.argv) <= 1:
        print(f"No arguments given, defaulting to simple style")
        main(SIMPLE_STYLE)

    elif args.bar:
        main(BAR_STYLE)

    elif args.divider:
        main(DIVIDER_STYLE)

    elif args.simple:
        main(SIMPLE_STYLE)

    elif args.style:
        style_path = args.style
        if not FileUtils.locate_file(style_path):
            print(f"Failed to locate input style file <{style_path}>!")
            print("Terminating...")
            sys.exit(1)

        main(style_path)


def main(style: str):
    try:
        generate_pdf(style)
    except FileNotFoundError as err:
        print(f"Ups! {err}")
        print("Terminating...")
        sys.exit(1)


if __name__ == '__main__':
    argparser = get_args()
    parse_args(argparser)

# TODO: Later we could consider abstracting to take o input file
#  instead of a default resume
