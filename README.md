# 🔐 Password Strength Analyzer + Cracker Simulator

A cybersecurity educational project that demonstrates how weak passwords can be analyzed and "simulated" for cracking using dictionary and brute-force methods.

---

## ⚠️ Disclaimer
This project is for **educational purposes only**.  
It does NOT perform real hacking or unauthorized access.

---

## 🚀 Features

- Password strength checker (zxcvbn)
- Dictionary attack simulation
- Brute-force simulation (limited safe demo)
- Terminal UI with rich formatting

---

## 📦 Installation

```bash
pip install -r requirements.txt
```

---

# 🐧 How to run on Linux

```bash id="run1"
sudo apt update
sudo apt install python3 python3-pip -y

pip install -r requirements.txt

python3 app.py
```

## WEB view

- go to any browser

```
http://localhost:5000/
```


## 🧠 How it works

- Weak passwords are tested against known patterns
- Dictionary attack uses common password lists
- Brute-force simulates guessing combinations


## 📁 Project Structure

- app.py → main program
- strength_checker.py → password analysis
- dictionary_attack.py → wordlist attack
- brute_force.py → brute-force simulation
- wordlists/ → password database

## 💡 Example Output
- Level: Weak
- Attempts: 152
- Time: 0.0023 sec

## ⭐ Future Improvements
- Web dashboard (Flask)
- Live attack animation
- Password entropy graphs




