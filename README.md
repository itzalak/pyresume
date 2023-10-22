# Markdown resume

This is a simple script to build a pdf resume based on a markdown file and css style.
It loads the default resume file, loads a css file from assets/styles folder and generates or overrides a pdf file to
output folder.

This package is mostly for testing stuff and generating my own resume, so you are probably lost...

## Credits

This code is just a wrapper for the work done by Julien Maupetit with [md2pdf](https://github.com/jmaupetit/md2pdf).

## Requirements

- Python
- Black
- Poetry
- Pre-commit

## Instructions

Instructions for setup can be found in the [makefile](./makefile)

## Examples

A style can be given as argument, if not, will default to a [simple style](pyresume/assets/styles/simple-style.css).
The resume markdown file can be found [here](pyresume/assets/resume.md).
Default style options are `-simple`, `-bar`, `-divider`, css for them can be found in [styles folder](pyresume/assets/styles/)

- Create a resume with simple look

```shell
make resume-simple
```

- Or with poetry

```shell
poetry run python pyresume/__main__.py -simple
```

- Run with path to a css style

```shell
poetry run pyresume/__main__.py --style {{path/to/user/style.css}}
```

### Tests

- Run all tests

```shell
poetry run pytest
```

- Run one class test

```shell
poetry run pytest tests/{{test_file_name}}.py
```
