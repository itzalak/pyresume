# Pyresume

This is a python script to build a pdf resume based on a markdown file and some given css style.

This package is just for documentation purposes and generating my own resume, if you found yourself here, you are probably
lost...

## Credits

This code is just a wrapper for the work done by Julien Maupetit with [md2pdf](https://github.com/jmaupetit/md2pdf).

## Requirements

- Python
- Black
- Poetry
- Pre-commit
- Commitizen
- Weasyprint

## Instructions

Instructions for setup can be found in the [makefile](./makefile)

## Examples

To generate a resume:

1. Place your resume file in `./pyresume/assets/resume.md`
2. Select a style from [style folder](./pyresume/assets/styles/) if none is selected defaults to [simple style](pyresume/assets/styles/simple-style.css)
3. Run the execution command from the examples below, like `make resume-simple`, or `poetry run python pyresume/__main__.py -bar`
4. Find the pdf resume under [output folder](./output)

- Create a resume with simple look using makefile

```shell
make resume-simple
```

- Or use poetry, available style options are `-simple`, `-bar`, `-divider`

```shell
poetry run python pyresume/__main__.py -simple
```

- Run with path to your own css style

```shell
poetry run pyresume/__main__.py --style {{path/to/user/style.css}}
```

### Tests

- Run all tests

```shell
poetry run pytest
```
