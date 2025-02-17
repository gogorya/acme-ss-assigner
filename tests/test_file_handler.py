import sys
import re

import pytest

from src.acme_ss_assigner import file_handler


# Testing valid terminal inputs
@pytest.mark.parametrize("data, output", [(["main.py", "current_year.csv", "previous_year.csv"],
                                           ["current_year.csv", "previous_year.csv"]),
                                          (["main.py", "current_year.csv"],
                                           ["current_year.csv"])])
def test_parse_files_valid(monkeypatch, data, output):
    monkeypatch.setattr(
        sys, "argv", data)
    result = file_handler.parse_files()
    assert result == output


# Testing invalid terminal inputs
@pytest.mark.parametrize("data", [["main.py"],
                                  ["main.py", "current_year.csv", "previous_year.csv", "extra.csv"]])
def test_parse_files_invalid(monkeypatch, data):
    monkeypatch.setattr(sys, "argv", data)
    with pytest.raises(ValueError, match=re.escape("Please enter files in format: main.py current_year.csv [previous_year.csv]")):
        file_handler.parse_files()
