from backend import db_helper

import os
import sys

print(__file__)


def test_db_helper():
    expenses= db_helper.fetch_expenses_for_date("2024-08-04")

    assert len(expenses) == 4
    assert expenses[0]['amount'] == 25

def test_fetch_expenses_for_date_invalid_date():
    expenses= db_helper.fetch_expenses_for_date("9999-08-04")

    assert len(expenses) == 0

def test_fetch_expense_summary_invalid_date():
    summary= db_helper.fetch_expense_summary("2099-08-04", "9999-08-04")
    assert len(summary) == 0