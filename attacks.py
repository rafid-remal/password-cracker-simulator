import time
import itertools
import string

# -----------------------------
# Dictionary Attack
# -----------------------------
def dictionary_attack(password, wordlist):
    attempts = 0
    start = time.time()

    for word in wordlist:
        attempts += 1
        if word.strip() == password:
            return {
                "success": True,
                "attempts": attempts,
                "time": time.time() - start
            }

    return {
        "success": False,
        "attempts": attempts,
        "time": time.time() - start
    }


# -----------------------------
# Brute Force (SAFE DEMO ONLY)
# limited to short passwords
# -----------------------------
def brute_force(password, max_len=3):
    chars = string.ascii_lowercase + string.digits
    attempts = 0
    start = time.time()

    for length in range(1, max_len + 1):
        for attempt in itertools.product(chars, repeat=length):
            attempts += 1
            guess = "".join(attempt)

            if guess == password:
                return {
                    "success": True,
                    "attempts": attempts,
                    "time": time.time() - start
                }

    return {
        "success": False,
        "attempts": attempts,
        "time": time.time() - start
    }
