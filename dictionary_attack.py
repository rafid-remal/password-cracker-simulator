import time

def dictionary_attack(password, wordlist):
    attempts = 0
    start = time.time()

    for word in wordlist:
        attempts += 1
        if word.strip() == password:
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
