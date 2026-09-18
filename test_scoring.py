"""
Tinker 1B, Part 1: write an assert-based pytest test for session_rating()
BEFORE you touch anything else. One test is started for you -- add at least
one more.
"""

from scoring import session_rating


def test_session_rating_boundary_90_is_great():
    assert session_rating(90) == "Great"


def test_session_rating_boundary_80_is_good():
    assert session_rating(80) == "Good"


def test_session_rating_boundary_70_is_ok():
    assert session_rating(70) == "OK"


def test_session_rating_boundary_60_is_meh():
    assert session_rating(60) == "Meh"


def test_session_rating_boundary_59_is_skip():
    assert session_rating(59) == "Skip"


def test_session_rating_negative_score():
    assert session_rating(-10) == "Skip"


def test_session_rating_over_100():
    assert session_rating(150) == "Great"


def test_session_rating_decimal_input():
    assert session_rating(87.5) == "Good"
