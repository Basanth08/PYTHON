import guessing_game
import random

def test_secret_number():
    seed = 1
    expected = 18

    actual = guessing_game.secret_number(seed)

    assert expected == actual

def test_too_low():
    n = 26
    a = 20

    actual = guessing_game.check_guess(n,a)

    assert actual == 'TOO LOW'


def test_correct():
    n = 26
    a = 26

    actual = guessing_game.check_guess(n,a)

    assert actual == 'CORRECT'


def test_too_high():
    n = 26
    a = 29

    actual = guessing_game.check_guess(n,a)

    assert actual == 'TOO HIGH'

def test_prompt_for_guess():
    s = guessing_game.secret_number(1)
    expected = 'CORRECT'

    actual = guessing_game.check_guess(s,18)
    
    assert actual == expected

def test_game():
    s = guessing_game.secret_number(8)
    expected = 'TOO HIGH'
    actual = guessing_game.check_guess(8,30)

    assert actual == expected
