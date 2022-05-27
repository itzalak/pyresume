# Markdown resume

This is a simple script to build a pdf resume based on a markdown file and css style.
It loads the default resume file, loads a css file from assets/styles folder and generates or overrides a pdf file to
output folder.

A style can be given as argument, if not, will default to a [simple style](markdown2pdf/assets/styles/simple-style.css).
The resume markdown file can be found [here](markdown2pdf/assets/resume.md).

*WARNING* this is a work in progress

## Credits

The core of the work is done by the package [md2pdf](https://github.com/jmaupetit/md2pdf).

# Instructions

- [how-to](#how-to)
    - [environment](#environment)
    - [run](#run)
    - [tests](#tests)

## How to

You can run this project with the following instructions, preferably running a virtual environment.
If running on MacOSX please be aware of the
following [issues](https://github.com/jmaupetit/md2pdf#troubleshooting-on-macosx)

### Environment

```shell
# Create a new environment
$ python3 -m venv venv

# Activate environment
$ source venv/bin/activate

# Install dependencies
$ pip install -r requirements.txt

# Deactivate
$ deactivate
```

### Run

Run default

```shell
$ python3 markdown2pdf/md_resume_to_pdf.py
```

Run with selected style

```shell
$ python3 markdown2pdf/main.py --style markdown2pdf/assets/styles/structured-style.css
```

### Tests

```shell
# Run all tests
$ pytest

# Run class test
$ pytest tests/<test_file_name>.py
```
