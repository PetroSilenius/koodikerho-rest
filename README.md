# Koodikerho REST

A python FastAPI exercise from Digit ry coding club held on 22.11.2021.
This repository consists of my result from the exercise and the
the original repository was authored by Eero Ruohola & Markus Blomqvist and can be found at [DigitKoodit/koodikerho-rest](git@github.com:DigitKoodit/koodikerho-rest.git).

### Requirements

- [Git](https://git-scm.com/downloads)
- [Python](https://www.python.org/downloads) (>=3.9)
- [Insomnia](https://insomnia.rest/download) (REST client, recommended for testing the API)

### Setup

1. **Clone this repo:**

```
git clone git@github.com:PetroSilenius/koodikerho-rest.git
```
OR
```
git clone https://github.com/PetroSilenius/koodikerho-rest.git
```

2. **Navigate to the directory you cloned:**

```
cd koodikerho-rest
```

3. **Create a Python virtual environment:**

(Use `python` or `python3` command depending on your system)
```
python -m venv venv
```

4. **Activate the virtual env:**

macOS, Linux, WSL, Git Bash:
```
source venv/bin/activate
```

Windows cmd.exe:
```
venv\Scripts\activate.bat
```

Windows PowerShell:
```
venv\Scripts\Activate.ps1
```

5. **Install the PyPI packages:**
```
pip install -r requirements.txt -r requirements-dev.txt
```

### Running

```
uvicorn main:app --reload
```
