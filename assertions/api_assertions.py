import pytest
import pytest_check as check


class APIAssertions:
    """Reusable assertions for API responses."""

    @staticmethod
    def assert_successful_bet(response: dict, request: dict) -> None:
        check.equal(response["message"], "Bet placed successfully")
        check.equal(response["matchId"], request["matchId"])
        check.equal(response["selection"], request["selection"])
        check.equal(response["stake"], request["stake"])

        check.is_true("odds" in response)
        check.is_true(response["odds"] > 0)

        check.is_true("payout" in response)
        check.equal(
            response["payout"],
            pytest.approx(response["stake"] * response["odds"])
        )

        check.is_true("balance" in response)

        check.is_true("currency" in response)
        check.equal(response["currency"], "EUR")

    @staticmethod
    def assert_balance_updated(
        initial_balance: float,
        updated_balance: float,
        stake: float,
    ) -> None:
        check.equal(updated_balance, initial_balance - stake)