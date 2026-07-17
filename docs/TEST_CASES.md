# Test Cases

---

## TC-001: Place a Single Bet

| Property | Value |
|----------|-------|
| **Feature** | Betting |
| **Domain** | UI |
| **Status** | ✅ Automated |
| **Priority** | High |

### Description

Verify that a user can successfully place a single bet from the home page.

### Test Scenario
```gherkin
    Given the user has a positive balance
    When the user selects the first available match
    And selects the Draw outcome
    And enters a stake of "10.00"
    And clicks the "Place Bet" button
    Then the bet should be accepted
    And the success popup should be displayed
```

### Expected Result

- Bet is successfully placed.
- Success popup is displayed.
- Bet receipt contains the selected event and stake.

---


## TC-002: Validate all fields in successful popup

| Property | Value |
|----------|-------|
| **Feature** | Betting |
| **Domain** | UI |
| **Status** | ✅ Automated |
| **Priority** | High |

### Description

Verify that success popup contains the same data as bet slip.

### Test Scenario
```gherkin
    Given the user has a positive balance
    When the user selects the first available match
    And selects the Draw outcome
    And enters a stake of "10.00"
    And clicks the "Place Bet" button
    And the success popup displayed
    Then success popup should  contain same data as Bet slip
```

### Expected Result

- Bet is successfully placed.
- Success popup is displayed.
- Success popup should contain the same data as Bet slip

---


## TC-003: Validate Potential Payout Calculation

| Property | Value |
|----------|-------|
| **Feature** | Betting |
| **Domain** | UI |
| **Status** | ✅ Automated |
| **Priority** | Medium |

### Description

Verify that the potential payout displayed in the bet slip is calculated as the stake multiplied by the selected odds.

### Test Scenario

```gherkin
    Given the user has a positive balance
    When the user selects the first available match
    And selects the Draw outcome
    And enters a stake of "10.00"
    Then the potential payout should equal the stake multiplied by the displayed odds
```

### Expected Result

- Potential payout is displayed.
- Potential payout equals **Stake × Odds**.
- Displayed payout matches the expected calculated value.

---

