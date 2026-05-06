import itertools
import string
import time

def brute_force(password):
    chars = string.ascii_lowercase + string.digits
    attempts = 0
    start = time.time()

    for length in range(1, 3):
        for attempt in itertools.product(chars, repeat=length):
            attempts += 1
            guess = "".join(attempt)

            if guess == password:
                return {
                    "success": True,
                    "attempts": attempts,
                    "time": round(time.time() - start, 4)
                }

    return {
        "success": False,
        "attempts": attempts,
        "time": round(time.time() - start, 4)
    }
