## Base Information
- Python = 3.9
- OS = Linux Mint 20.1 Cinnamon (4.8.6)
- Chromedriver = 96 (You will need to download and place the chromedriver that matches your browser in this directory)

## Setup New Virtual Environment
In the root directory of the project (for ease of access) run
```bash
python3 -m venv name_of_your_environment
```

Open terminal in proquest_exercise folder and run
```bash
. virtual_env/bin/activate
```

To install needed libraries run
```bash
pip install -r requirements.txt
```

## Run Tests
The simplest way to run the suite is
```bash
python -m pytest tests/
```

If you want to run with the browser in headless mode simply add --headless to the parameters.
```bash
python -m pytest tests/ --headless
```
