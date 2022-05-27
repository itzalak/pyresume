import argparse

from md_resume_to_pdf import main

# TODO: It would be better if I could add standard styles as arguments
#  Like --bars, --simple, --structured and --style for other options
#  Look for mutual exclusive arguments

# TODO: update resume

# TODO: Default is not working!
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create a pdf resume')
    parser.add_argument('--style', metavar='path', required=False,
                        help='style name')
    args = parser.parse_args()

    main(args.style)

# TODO: Later we could consider abstracting to take o input file
#  instead of a default resume

# TODO: Use exceptions

# TODO: how about logging?
