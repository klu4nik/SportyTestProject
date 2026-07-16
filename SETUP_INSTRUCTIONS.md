# Setup Instructions

## Prerequisites
- Python 3.12+
- Chrome Browser

## Installation Steps

1. Create a virtual environment:
```bash
python -m venv .venv
```

2. Activate the virtual environment:
```bash
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install ChromeDriver (if not already installed):
```bash
# On macOS with Homebrew
brew install chromedriver

# Or download from https://chromedriver.chromium.org/
```

## Running Tests

You can run tests from any directory using the provided script:

```bash
./run_tests.sh
```

Or to run a specific test file:
```bash
./run_tests.sh tests/ui/test_place_single_bet.py
```

Alternatively, you can run pytest directly from the project root directory:
```bash
pytest
```

Run UI tests only:
```bash
pytest tests/ui/ -v
```

Run API tests only:
```bash
pytest tests/api/ -v
```

Generate HTML report:
```bash
pytest --html=report.html --self-contained-html
```

## Project Structure

```
qae-assignment/
├── README.md
├── requirements.txt
├── pytest.ini
├── .gitignore
├── docs/
│   ├── TEST_PLAN.md
│   ├── EXECUTION_RESULTS.md
│   └── STRATEGY.md
├── pages/
│   ├── base_page.py
│   ├── home_page.py
│   └── bet_slip_page.py
├── locators/
│   ├── home.py
│   └── bet_slip.py
├── api/
│   ├── api_client.py
│   ├── balance_api.py
│   └── endpoints.py
├── tests/
│   ├── ui/
│   │     test_place_single_bet.py
│   │
│   └── api/
│         test_place_bet_validation.py
├── utils/
│   └── config.py
├── screenshots/
└── conftest.py