from logic_utils import check_guess

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


def test_too_high_hint_tells_player_to_go_lower():
    # Regression test for the swapped-hint bug.
    # Reported case: guess 48 vs secret 34. The guess is too high, so the
    # hint MUST tell the player to go LOWER (the bug said "Go HIGHER!").
    outcome, message = check_guess(48, 34)

    assert outcome == "Too High"
    assert "LOWER" in message, f"expected a 'go lower' hint, got: {message!r}"
    assert "HIGHER" not in message, f"hint wrongly tells player to go higher: {message!r}"
