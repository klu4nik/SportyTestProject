# Bug Reports

This document contains defects identified during automated UI and API test execution.

---

## BUG-001: `place_bet` API accepts negative stake values

| Property | Value |
|----------|-------|
| **Severity** | Critical |
| **Priority** | Critical |
| **Area** | API / Business Logic |
| **Related Test Case** | TC-006 |

### Summary

The `place_bet` endpoint accepts a negative stake value, resulting in the user's account balance increasing instead of decreasing.

### Preconditions

- User has a positive account balance.
- At least one valid match is available.

### Steps to Reproduce

1. Send a `POST /place_bet` request.
2. Use a valid `matchId` and selection.
3. Set the stake to `-2`.
4. Submit the request.

### Expected Result

- The request is rejected with a validation error.
- An appropriate error message is returned.
- The account balance remains unchanged.

### Actual Result

- The request is accepted.
- The account balance increases instead of decreasing.

### Impact

This allows users to artificially increase their balance, representing a critical business logic and security vulnerability.

---

## BUG-002: Currency mismatch in `place_bet` API response

| Property | Value |
|----------|-------|
| **Severity** | High |
| **Priority** | High |
| **Area** | API |
| **Related Test Case** | TC-005 |

### Summary

The currency returned by the `place_bet` endpoint does not match the expected account currency.

### Preconditions

- User has a valid account.
- User places a valid bet.

### Steps to Reproduce

1. Reset the account balance.
2. Place a valid bet using the API.
3. Inspect the response body.

### Expected Result

The response contains the correct account currency (`EUR`).

### Actual Result

The returned currency differs from the expected value.

### Impact

The API response is inconsistent and may cause incorrect balance presentation or downstream integration issues.

---

## BUG-003: Account balance is not updated in the UI after successful bet placement

| Property | Value |
|----------|-------|
| **Severity** | High |
| **Priority** | High |
| **Area** | UI |
| **Related Test Case** | TC-001 |

### Summary

After successfully placing a bet, the balance displayed in the UI remains unchanged.

### Preconditions

- User has sufficient balance.
- User successfully places a bet.

### Steps to Reproduce

1. Open the Sports Home page.
2. Place a valid bet.
3. Close the confirmation popup.
4. Observe the account balance displayed in the header.

### Expected Result

The displayed balance decreases by the stake amount.

### Actual Result

The displayed balance remains unchanged.

### Impact

The UI shows outdated account information and is inconsistent with the backend.

---

## BUG-004: Confirmation popup displays incorrect bet details

| Property | Value |
|----------|-------|
| **Severity** | High |
| **Priority** | High |
| **Area** | UI |
| **Related Test Case** | TC-001 |

### Summary

The confirmation popup displays values that differ from those shown in the bet slip before placing the bet.

### Preconditions

- User places a valid bet.

### Steps to Reproduce

1. Select any available match.
2. Enter a valid stake.
3. Note the stake, odds, and potential payout displayed in the bet slip.
4. Place the bet.
5. Compare the confirmation popup with the bet slip.

### Expected Result

The confirmation popup displays exactly the same:

- Stake
- Odds
- Potential payout

### Actual Result

One or more values differ from those displayed in the bet slip.

### Impact

Users receive inconsistent betting information after placing a bet.

---

## BUG-005: Historical matches are available for betting

| Property | Value |
|----------|-------|
| **Severity** | Critical |
| **Priority** | Critical |
| **Area** | UI / API / Business Logic |
| **Related Test Case** | TC-004 |

### Summary

Completed (historical) matches are displayed in the match list and still allow users to place bets.

### Preconditions

- Historical matches exist in the system.

### Steps to Reproduce

1. Open the Sports Home page.
2. Select the **All** filter.
3. Locate a historical match.
4. Attempt to place a bet.

### Expected Result

- Historical matches should not be displayed as available for betting.
- Betting controls should be disabled for completed matches.

### Actual Result

Historical matches are displayed and users can successfully place bets on them.

### Impact

Users can place bets on completed events, violating core betting business rules and potentially leading to invalid transactions.