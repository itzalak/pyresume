# Markdown resume

This is a simple script to build a pdf resume based on a markdown file and css style.
It looks for a `resume.md` file, loads a css file from styles folder and generates or overrides a pdf file to output
folder.

A style can be given as argument, if not will default to a [simple style](assets/styles/simple-style.css).
The resume markdown file can be found [here](assets/resume.md).

*WARNING* this is a work in progress

## Credits

The core of the work is done by the package [md2pdf](https://github.com/jmaupetit/md2pdf).

# Instructions

- [how-to](#how-to)
    - [environment](#environment)
    - [requirements](#requirements)
        - [pip freeze](#pip-freeze)
        - [pip tools](#pip-tools)
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

### Requirements

#### Pip freeze

```shell
# Create a requirements file from all installed modules and versions
# If file exist it will need to be deleted
$ pip freeze > requirements.txt

# List outdated packages
$ pip list --outdated

# Update one package
$ pip install -U <package-name>

# Update all
$ pip install -U -r requirements.txt

# Check missing dependencies
$ python -m pip check
```

#### Pip tools

```shell
# Install pip-tools
$ pip install pip-tools

# Generate requirements.txt
$ pip-compile requirements.in

# Update requirements.txt
$ pip-compile --upgrade

# Update single package
$ pip-compile --upgrade-package <package-name>

# Update single package to a specific version
# e.g. --upgrade-package requests==2.0.0
$ pip-compile --upgrade-package <package-name>==<version>
```

### Run

Run default

```shell
$ python3 md_resume_to_pdf.py
```

Run with selected style

```shell
$ python3 build_pdf_resume.py styles/bar-style.css
```

### Tests

```shell
# Run all tests
$ pytest

# Run class test
$ pytest tests/<test_file_name>.py
```
