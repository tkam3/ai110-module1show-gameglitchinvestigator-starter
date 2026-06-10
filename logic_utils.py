def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        # FIXME (fixed): Hard used 1-50, which was narrower/easier than Normal.
        # FIX: widened to 1-200 — I described the symptom and the AI proposed the range.
        return 1, 200
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return the outcome string.

    Returns one of: "Win", "Too High", "Too Low".
    """
    # FIXME (fixed): secret was stringified on even turns in app.py, so a
    # correct guess never matched (42 == "42" is False). Now both are ints.
    # FIX: AI explained the int-vs-str comparison; I removed the str() cast in app.py.
    if guess == secret:
        return "Win"
    if guess > secret:
        return "Too High"
    return "Too Low"


def hint_message(outcome: str):
    """Return the player-facing hint for an outcome."""
    # FIXME (fixed): the higher/lower hints were swapped. A guess that is
    # too high should tell the player to go LOWER, and vice versa.
    # FIX: refactored hint text out of check_guess into this helper (agent mode).
    if outcome == "Win":
        return "🎉 Correct!"
    if outcome == "Too High":
        return "📉 Go LOWER!"
    return "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        # FIXME (fixed): winning on the first attempt now scores 100.
        # FIX: AI first miscalculated (said 80), I caught it; together we traced
        # the two off-by-one errors and corrected the formula to (attempt - 1).
        points = 100 - 10 * (attempt_number - 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
