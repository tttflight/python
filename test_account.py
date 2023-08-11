import pytest
from account import Account


def test_init():
    account = Account("Will Thompson")
    assert account.get_name() == "Will Thompson"
    assert account.get_balance() == 0


def test_deposit():
    account = Account("Lauren Frazier")
    account.deposit(2000)
    assert account.get_balance() == 2000


def test_withdraw():
    account = Account("David Kay")
    account.deposit(2000)
    account.withdraw(1000)
    assert account.get_balance() == 1000


def test_account_withdraw_fail():
    account = Account("Mallory Pane")
    account.deposit(2000)
    result = account.withdraw(3000)
    assert result is False
    assert account.get_balance() == 2000


if __name__ == "__main__":
    pytest.main()
