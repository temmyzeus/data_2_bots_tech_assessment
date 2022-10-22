## Using Pip
Create virtual environment with either virtualenv or venv using python3.9. Then run `pip install -r requirements.txt` to install dependencies.

Then run actual program with:
```bash
python main.py
```

## Using Poetry

Run below command to create virtual environment with poetry
```bash
poetry shell
```
To install dependencies
```bash
poetry install
```
If using Poetry's `poetry run`, first run `chmod +x main.py` to make file an executable.

Then run actual program with:
```bash
python main.py
```
