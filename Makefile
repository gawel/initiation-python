all: install notebook

notebook:
	venv/bin/jupyter notebook

install: venv
	venv/bin/pip install -r requirements.txt

venv:
	python3 -m venv venv
	venv/bin/pip install -U pip wheel

