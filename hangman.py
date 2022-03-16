import random

def get_secret_word(wordfile="/usr/share/dict/words"):
    """
    Returns a secret word obeying the following rules
    1. Cannot be a proper noun (shouldn't start with a capital letter)
    2. Should not be less than 4 or more than 10 letters long
    3. Should not have any punctuation
    """
    good_words = []
    with open(wordfile) as f:
        for w in f:
            w = w.strip()
            if w[0].isupper():
                continue
            if len(w) < 4 or len(w) >= 10:
                continue
            if not w.isalpha():
                continue
            good_words.append(w)
    return random.choice(good_words)

def mask_word(word, guesses):
    op = []
    for i in word:
        if i in guesses:
            op.append(i)
        else:
            op.append("-")
    return "".join(op)

def create_status(secret_word, guesses, rem_turns):
    masked_word = mask_word(secret_word, guesses)
    guesses = " ".join(guesses)
    return f"""Word: {masked_word}
Guesses: {guesses}
Remaining turns : {rem_turns}
"""

def play_round(secret_word, guesses, guess, rem_turns):
    if "-" not in mask_word(secret_word, guesses+[guess]):
        return rem_turns, False, True
    if guess in guesses:
        return rem_turns, True, False
    if guess in secret_word:
        guesses.append(guess)
        return rem_turns, False, False
    if guess not in secret_word:
        guesses.append(guess)
        return rem_turns-1, False, False

def main():
    print ("Welcome to Hangman")
    secret_word = get_secret_word()
    print (secret_word)
    rem_turns = 7
    guesses = []
    while True:
        status = create_status(secret_word, guesses, rem_turns)
        print (status)
        guess = input("Enter a letter ").strip()
        rem_turns, repeat, finished = play_round(secret_word, guesses, guess, rem_turns)
        if finished:
            print (f"You found the secret word '{secret_word}'")
            break
        if rem_turns == 0:
            print (f"You failed. The secret word was {secret_word}")
            break
        elif repeat:
            print (f"You already guessed '{guess}'")

if __name__ == "__main__":
    main()