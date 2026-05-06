from zxcvbn import zxcvbn

def check_strength(password):
    r = zxcvbn(password)

    levels = ["Very Weak", "Weak", "Fair", "Good", "Strong"]

    return {
        "score": r["score"],
        "level": levels[r["score"]],
        "guesses": r["guesses"]
    }
