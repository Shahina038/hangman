import random

import hangman

random.seed(42)

def test_secret_word_no_proper_noun():
    with open("/tmp/wordlist.txt", "w") as f:
        f.write("apple\n")
        f.write("Grape\n")
        f.write("Watermelon\n")
    for _ in range(10):
        word = hangman.get_secret_word("/tmp/wordlist.txt")
        assert word == "apple"

def test_secret_word_correct_length():
    with open("/tmp/wordlist.txt", "w") as f:
        f.write("ape\n")
        f.write("table\n")
        f.write("mattresses\n")
    for _ in range(20):
        word = hangman.get_secret_word("/tmp/wordlist.txt")
        assert word == "table"

def test_secret_word_no_punctuation():
    with open("/tmp/wordlist.txt", "w") as f:
        f.write("spain's\n")
        f.write("america's\n")
        f.write("india\n")
    for _ in range(20):
        word = hangman.get_secret_word("/tmp/wordlist.txt")
        assert word == "india"
 
def test_mask_word_bad_guess():
    assert hangman.mask_word("hangman", ["x"]) == "-------"

def test_mask_word_good_guess_single():
    assert hangman.mask_word("hangman", ["h"]) == "h------"

def test_mask_word_good_guess_multiple():
    assert hangman.mask_word("hangman", ["a"]) == "-a---a-"

def test_mask_word_good_guess_mix():
    assert hangman.mask_word("hangman", ["a", "x", "h"]) == "ha---a-"

def test_create_status_normal():
    secret_word = "hangman"
    guesses = ["a", "x", "h"]
    remaining_turns = 4
    assert hangman.create_status(secret_word, guesses, remaining_turns) == """Word: ha---a-
Guesses: a x h
Remaining turns : 4
"""

def test_create_status_no_guesses():
    secret_word = "hangman"
    guesses = []
    remaining_turns = 7
    status = hangman.create_status(secret_word, guesses, remaining_turns)
    assert status == """Word: -------
Guesses: 
Remaining turns : 7
"""

def test_play_round_correct_guess():
    secret_word = "hangman"
    guesses = []
    remaining_turns = 4
    guess = "a"
    remaining_turns, repeat, finished = hangman.play_round(secret_word, guesses, guess, remaining_turns)
    assert guesses == ["a"]
    assert remaining_turns == 4
    assert repeat == False
    assert finished == False

def test_play_round_correct_repeat():
    secret_word = "hangman"
    guesses = ["a"]
    remaining_turns = 4
    guess = "a"
    remaining_turns, repeat, finished = hangman.play_round(secret_word, guesses, guess, remaining_turns)
    assert guesses == ["a"]
    assert remaining_turns == 4
    assert repeat == True
    assert finished == False

def test_play_round_correct_wrong():
    secret_word = "hangman"
    guesses = ["a"]
    remaining_turns = 7
    guess = "x"
    remaining_turns, repeat, finished = hangman.play_round(secret_word, guesses, guess, remaining_turns)
    assert guesses == ["a", "x"]
    assert remaining_turns == 6
    assert repeat == False
    assert finished == False

def test_play_round_correct_complete():
    secret_word = "hangman"
    guesses = ["h", "a", "n", "g", "m"]
    remaining_turns = 7
    guess = "n"
    remaining_turns, repeat, finished = hangman.play_round(secret_word, guesses, guess, remaining_turns)
    assert finished == True
    