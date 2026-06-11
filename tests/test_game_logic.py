from logic_utils import (
    check_guess,
    hint_message,
    get_range_for_difficulty,
    update_score,
    parse_guess,
)

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


# --- Tests targeting the bugs we fixed ---

def test_hint_messages_point_toward_secret():
    # Bug: higher/lower hints were swapped. Too High should say go LOWER.
    assert hint_message("Too High") == "📉 Go LOWER!"
    assert hint_message("Too Low") == "📈 Go HIGHER!"

def test_hard_is_harder_than_normal():
    # Bug: Hard's range (1-50) was narrower than Normal (1-100).
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high > normal_high

def test_first_attempt_win_scores_100():
    # Bug: a first-attempt win scored 70 instead of 100.
    assert update_score(0, "Win", attempt_number=1) == 100
    assert update_score(0, "Win", attempt_number=2) == 90


# --- Edge cases ---

def test_parse_guess_rejects_empty_and_non_numeric():
    # Edge case: blank input and garbage text should fail gracefully,
    # not crash, and should report ok=False with an error message.
    ok, value, err = parse_guess("")
    assert ok is False and value is None and err == "Enter a guess."

    ok, value, err = parse_guess("abc")
    assert ok is False and value is None and err == "That is not a number."

def test_parse_guess_truncates_decimals():
    # Edge case: a decimal like "3.9" should parse to the int 3, not crash.
    ok, value, err = parse_guess("3.9")
    assert ok is True
    assert value == 3
    assert err is None

def test_win_score_never_drops_below_floor():
    # Edge case: winning very late should not give negative or tiny points;
    # the score is floored at 10 no matter how many attempts it took.
    assert update_score(0, "Win", attempt_number=20) == 10


# --- Challenge 1: advanced edge cases ---

def test_negative_number_is_handled():
    # Edge case: a negative guess should parse without crashing and, since it's
    # below any valid secret, be treated as "Too Low" rather than breaking.
    ok, value, err = parse_guess("-7")
    assert ok is True
    assert value == -7
    assert check_guess(value, 50) == "Too Low"

def test_extremely_large_number_is_handled():
    # Edge case: a huge number (far beyond the range) should parse and be
    # reported as "Too High" instead of overflowing or erroring.
    ok, value, err = parse_guess("99999999999999999999")
    assert ok is True
    assert value == 99999999999999999999
    assert check_guess(value, 50) == "Too High"

def test_whitespace_padded_number_is_handled():
    # Edge case: extra spaces around a number (e.g. from copy/paste) should
    # still parse to the correct int rather than being rejected.
    ok, value, err = parse_guess("  42  ")
    assert ok is True
    assert value == 42
    assert err is None
