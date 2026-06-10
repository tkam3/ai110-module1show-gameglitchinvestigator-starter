from logic_utils import (
    check_guess,
    hint_message,
    get_range_for_difficulty,
    update_score,
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
