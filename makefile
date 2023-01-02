# Makefile

VENV = mk-venv
ACTIVATION = $(VENV)/bin/activate

venv: python-install-requirements

python-install-requirements: python-update-requirements
	. $(ACTIVATION) && pip3 install -r requirements.txt

python-update-requirements: python-create-venv
	. $(ACTIVATION) && pip-compile --upgrade requirements.in

python-create-venv: python-delete-venv
	python3 -m venv $(VENV)

python-delete-venv:
	rm -rf $(VENV)
	rm -rf venv

resume-bar:
	. $(ACTIVATION) && python3 markdown2pdf/__main__.py -bar

resume-simple:
	. $(ACTIVATION) && python3 markdown2pdf/__main__.py -simple

resume-divider:
	. $(ACTIVATION) && python3 markdown2pdf/__main__.py -divider
