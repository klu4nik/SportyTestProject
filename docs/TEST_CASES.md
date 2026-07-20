# Test Cases

---

## TC-001: Place a Single Bet and Validate Bet Details

| Property | Value       |
|----------|-------------|
| **Feature** | Betting     |
| **Domain** | UI + API    |
| **Status** | ✅ Automated |
| **Priority** | Critical    |

### Description

Verify that a user can successfully place a single bet, that all values displayed during the betting flow are correct, and that the account balance is updated after the bet is placed.

### Risk Rationale

Placing a bet is the core business workflow. If this functionality fails, users cannot use the platform, making it the highest-risk scenario.


### Test Scenario

```gherkin
Given the user has a positive account balance
And the user opens the Sports Home page
When the user selects a match outcome
And enters a valid stake
And places the bet
Then the bet should be accepted successfully
And a success confirmation popup should be displayed
And the popup stake should match the bet slip stake
And the popup odds should match the bet slip odds
And the popup potential payout should match the bet slip potential payout
And the potential payout should equal Stake × Odds
And the account balance returned by the API should decrease by the stake amount
And the account balance displayed in the UI should decrease by the stake amount
```

### Test Data

| Parameter | Values                       |
|----------|------------------------------|
| Match | First available match        |
| Outcome | Home (0), Draw (1), Away (2) |
| Stake | €1, €30.5, €100              |

**Total Executions:** 9 (3 outcomes × 3 stake values)

### Expected Results

- The bet is accepted successfully.
- A success confirmation popup is displayed.
- The popup stake matches the stake entered in the bet slip.
- The popup odds match the odds displayed in the bet slip.
- The popup potential payout matches the value displayed in the bet slip.
- The potential payout is calculated correctly using the formula:

  ```
  Potential Payout = Stake × Odds
  ```

- The account balance returned by the API equals:

  ```
  Initial Balance − Stake
  ```

- The account balance displayed in the UI equals:

  ```
  Initial Balance − Stake
  ```

- The balances shown in the UI and returned by the API are consistent.

### Automation Notes

- The account balance is reset before each test execution.
- The test is parameterized to validate three betting outcomes and six stake values (18 executions).
- Bet slip values are captured before placing the bet because the confirmation popup replaces the bet slip.
- Soft assertions (`pytest-check`) are used to validate all popup fields, payout calculation, and balance updates within a single execution, allowing all failures to be reported together.


## TC-002: Validate different negative values of bets

| Property | Value |
|----------|-------|
| **Feature** | Betting |
| **Domain** | UI  |
| **Status** | Not automated |
| **Priority** | High |

### Description

Verify that a user can't place a bet using invalid stake values

### Risk Rationale

Invalid stake validation protects against incorrect user input and prevents invalid financial transactions.

### Test Scenario

```gherkin
Given the user has a positive account balance
And the user opens the Sports Home page
When the user selects a match outcome
And enters an invalid stake
Then the error message near stake field must be shown or input block wrong values
```

### Test Data

| Parameter | Values                       |
|----------|------------------------------|
| Match | First available match        |
| Outcome | Home (0) |
| Stake | -€2, €0, €0.99, €30.9954, €100.11, "Eleven"   |

**Total Executions:** 6

### Expected Results

- Error message shown or wrong data not placed


### Automation Notes

- The account balance is reset before each test execution.
- The test is parameterized to validate multiple incorrect values
- Some steps  can be moved to preconditions

## TC-003: Validate low balance messages

| Property | Value |
|----------|-------|
| **Feature** | Betting |
| **Domain** | UI  |
| **Status** | Not automated |
| **Priority** | High |

### Description

Verify that a user can't place a bet with incorrect values

### Risk Rationale

Allowing bets without a sufficient balance could result in incorrect account states and financial inconsistencies.

### Test Scenario

```gherkin
Given the user has a positive account balance 120€
And the user opens the Sports Home page
And the user selects a match outcome
And enters a valid stake 100€
And succesfully place bet
And closed successful popup
When the user selects a match outcome
And enters a valid stake 30€
Then the error message "Insufficient balance" near stake field must be shown
```

### Expected Results

- The error message "Insufficient balance" near stake field must be shown


### Automation Notes

- The account balance is reset before each test execution.



## TC-004: Validate matches search and dates filters

| Property | Value |
|----------|-------|
| **Feature** | Matches |
| **Domain** | UI + API |
| **Status** | Not automated |
| **Priority** | High |

### Description

Validate matches list shows correct values for the search and dates filters

### Risk Rationale

Incorrect filtering may display unavailable or historical events, leading users to place bets on invalid matches.

### Test Scenario

```gherkin
Scenario Outline: Verify date filters display correct matches

Given the user has retrieved the list of matches from the Matches API
And the user opens the Sports Home page
When the user selects the "<filter>" date filter
Then only "<expected_matches>" matches are displayed

Examples:
| filter      | expected_matches |
| All         | future           |
| Current Day | current day      |
| Next Day    | next day         |
| Next Week   | next week        |
```

### Expected Results

- Only relevant upcoming matches shown


## TC-005: Place a Single Bet via API and Validate Bet Details

| Property | Value     |
|----------|-----------|
| **Feature** | Betting   |
| **Domain** | API       |
| **Status** | Automated |
| **Priority** | High      |

### Description

Validate matches list shows correct values for the search and dates filters

### Risk Rationale

The API is the source of truth for bet placement. Incorrect responses affect all clients using the service.

### Test Scenario

```gherkin
Given the user has a positive account balance
When the user sends Place_bet api request with correct body and stake
Then response comes with 200 response code 
And response body contain correct information
And balance is correct 
And currency is "Eur"
```
### Test Data

| Parameter | Values                       |
|----------|------------------------------|
| Match | First available match        |
| Outcome | Home (0), Draw (1), Away (2) |
| Stake | €1, €30.5, €100              |

### Expected Results

- Response validates, according to the swagger collections, and contains the right balance and currency

## TC-006: Place an incorrect Single Bet via API and Validate Error

| Property | Value     |
|----------|-----------|
| **Feature** | Betting   |
| **Domain** | API       |
| **Status** | Automated |
| **Priority** | Critical  |

### Description

Validate matches list shows correct values for the search and dates filters

### Test Scenario


```gherkin
Given the user has a positive account balance
When the user sends place_bet api request with correct body and incorrect stake
Then response comes with error responce code shown
And response body contain minimum or incorrect format stake error message

```
### Test Data

| Parameter | Values                       |
|----------|------------------------------|
| Match | First available match        |
| Stake | -€2, €0, €0.99, €30.9954, €100.11, "Eleven"    |

### Expected Results

- A validation error message is displayed.
- Invalid values cannot be submitted.
- The bet is not placed.
- The account balance remains unchanged.

