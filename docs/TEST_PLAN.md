# Test Plan

## Purpose

The purpose of this project is to verify the core betting functionality through a combination of UI and API tests. The focus is on the main user flow and the most important business rules rather than exhaustive test coverage.

## Scope

### UI

- Place a single bet
- Verify bet confirmation popup
- Verify stake, odds and potential payout
- Verify account balance after a successful bet

### API

- Get available matches
- Place a valid bet
- Validate response data
- Verify account balance
- Validate incorrect stake values

### Manual Scenarios

The following scenarios were prepared but not automated:

- Invalid stake validation
- Insufficient balance
- Match search and date filters

## Test Environment

- Python 3.12
- Pytest
- Selenium WebDriver
- Requests
- Google Chrome (latest)
- pytest-html

## Test Data

The tests use:

- the first available match returned by the API
- Home, Draw and Away outcomes
- valid and invalid stake values

The account balance is reset before every test to keep executions independent.

## Running the Tests

Run everything:

```bash
pytest
```

Run only UI tests:

```bash
pytest -m ui
```

Run only API tests:

```bash
pytest -m api
```

Generate an HTML report:

```bash
pytest --html=reports/report.html --self-contained-html
```

## Notes

The framework uses the Page Object Model for UI tests and separates UI, API, assertions and fixtures into independent modules. Parameterized tests are used where the same scenario needs to be executed with different input values. Soft assertions (`pytest-check`) are used in UI validation to report all failed checks in a single execution instead of stopping on the first failure.