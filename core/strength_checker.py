from zxcvbn import zxcvbn

def check_strength(password):
    result = zxcvbn(password)

    levels = [
        "Very Weak",
        "Weak",
        "Fair",
        "Good",
        "Strong"
    ]

    return {
        "score": result["score"],
        "level": levels[result["score"]],
        "guesses": result["guesses"],
        "crack_time": result["crack_times_display"]["offline_slow_hashing_1e4_per_second"]
    }
