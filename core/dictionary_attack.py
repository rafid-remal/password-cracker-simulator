import time

def dictionary_attack(password, wordlist):
    attempts = 0
    start = time.time()

    for word in wordlist:
        attempts += 1
        word = word.strip()

        if word == password:
            return {
                "success": True,
                "attempts": attempts,
                "time": round(time.time() - start, 4),
                "found_password": word
            }

    return {
        "success": False,
        "attempts": attempts,
        "time": round(time.time() - start, 4),
        "found_password": None
    }

