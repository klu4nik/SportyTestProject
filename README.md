# QA Automation Take-Home Assignment

This project implements a test automation framework for a sports betting platform using Python, Selenium, and Pytest.

## Project Overview

A lightweight, maintainable test automation framework following Python best practices with Page Object Model design pattern. The framework supports both UI and API testing with proper fixtures, configuration management, and reporting capabilities.

## Prerequisites

- Python 3.12+
- Chrome Browser

## Installation

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
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

To generate HTML report:
```bash
pytest --html=report.html --self-contained-html
```

## Configuration

The following environment variables can be configured in `utils/config.py`:

- `USER_ID` - User identifier for test execution. Need to be setted up in env or modified in utils/config.py file

## Project Structure

```
/
│
├── README.md
├── requirements.txt
├── pytest.ini
├── .gitignore
│
├── docs/
│   ├── TEST_PLAN.md
│   ├── EXECUTION_RESULTS.md
│   └── STRATEGY.md
│
├── pages/
│   ├── base_page.py
│   ├── home_page.py
│   └── bet_slip_page.py
│
├── locators/
│   ├── home.py
│   └── bet_slip.py
│
├── api/
│   ├── api_client.py
│   ├── balance_api.py
│   └── endpoints.py
│
├── tests/
│   ├── ui/
│   │     test_place_single_bet.py
│   │
│   └── api/
│         test_place_bet_validation.py
│
├── utils/
│   └── config.py
│
├── screenshots/
│
└── conftest.py
```

## Framework Features

- Page Object Model for UI tests
- Separate API client layer
- Reusable assertion helpers
- Pytest fixtures for setup and cleanup
- Parameterized test execution
- Soft assertions with `pytest-check`
- HTML reporting
- Automatic screenshots on UI failures


## Documentation

Additional documentation is available in the `docs` directory:

- `TEST_PLAN.md`
- `TEST_CASES.md`
- `EXECUTION_RESULTS.md`
- `BUGS.md`

---