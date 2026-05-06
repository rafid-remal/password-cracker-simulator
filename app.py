from flask import Flask, render_template, request
from core.strength_checker import check_strength
from core.dictionary_attack import dictionary_attack
from core.brute_force import brute_force

app = Flask(__name__)

def load_wordlist():
    try:
        with open("wordlists/common_passwords.txt") as f:
            return f.readlines()
    except:
        return ["123456", "password", "admin"]

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/check", methods=["POST"])
def check():
    password = request.form["password"]
    mode = request.form["mode"]

    strength = check_strength(password)

    result = {
        "password": password,
        "strength": strength
    }

    wordlist = load_wordlist()

    if mode == "dictionary":
        attack = dictionary_attack(password, wordlist)
        result["attack"] = attack

    elif mode == "bruteforce":
        attack = brute_force(password)
        result["attack"] = attack

    return render_template("result.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
