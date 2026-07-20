# Execution Results

## Test Run Summary

This document provides results from test executions.

### Recent Test Runs

| Date       | Tests Executed | Pass Rate | Notes                           |
|------------|----------------|-----------|---------------------------------|
| 2026-07-18 | UI and API tests | 46%       | Critical failures in validation |

## Test Coverage

### Tests execution

| Test Case | Automation | Result |
|-----------|------------|--------|
| TC-001: Place a Single Bet and Validate Bet Details | 🤖 Automated | ❌ Failed |
| TC-002: Validate Different Negative Values of Bets | 📝 Manual | ✅ Passed* |
| TC-003: Validate Low Balance Messages | 📝 Manual | ✅ Passed* |
| TC-004: Validate Matches Search and Date Filters | 📝 Manual | ❌ Failed* |
| TC-005: Place a Single Bet via API and Validate Bet Details | 🤖 Automated | ❌ Failed |
| TC-006: Place an Incorrect Single Bet via API and Validate Error | 🤖 Automated | ⚠️ Partially Passed (5/6) |   
  
### TC-006 Execution Details

| Test Instance | Result |
|--------------|--------|
| stake_-2 | ❌ Failed |
| stake_0 | ✅ Passed |
| stake_0.99 | ✅ Passed |
| stake_30.9954 | ✅ Passed |
| stake_100.11 | ✅ Passed |
| stake_Eleven | ✅ Passed |

## Issues and Defects

The latest execution identified several issues:

- **Critical Security/Business Logic Issue:** The `place_bet` endpoint accepts a negative stake, allowing the account balance to increase instead of decrease.
- Currency mismatch between expected and actual values in API for place bet endpoint.
- Balance was not updated after bet placement in ui.
- Popup values did not match the bet slip.
- **Critical Security/Business Logic Issue:** Matches list shows historical matches, and you are able to place a bet for it

