# Task6
# Task 6 - Password Strength Analysis - Elevate Labs Internship

## Objective
Understand why password complexity matters.

## What I Did
1. Created 5 passwords with increasing complexity
2. Tested on passwordmeter.com
3. Built my own Python checker (check screenshots)

## Key Results
| Password Example | Strength | Time to Crack |
|---|---|---|
| Sukanya | Very Weak | 4 seconds |
| Sukanya124 | Fair | 1 month |
| Sukanya124@2**3 | Strong but Date pattern | Easily guessed |
| eoiqn6h46i0yFaJL (16-char random) | Very Strong | >1 Trillion Years |

## Learning
- Length > Complexity - 16 chars must
- Never use Name + DOB - Tool flagged "Contains a date"
- Use Upper + Lower + Number + Symbol

Tools: passwordmeter.com + Python (re, math)
```
1. Sukanya -> Score 14% - Very Weak - 4 seconds to crack

2. Sukanya124 -> Score 56% - Fair - 1 month to crack

3. Sukanya124@2003 -> Score 85% - Strong 
   Warning: Contains a date, easily guessed

4. Sukanya124@2*3 -> Score 100% - Strong 
   Warning: Still contains name pattern

5. eoiqn6h46i0yFaJL -> Score 100% - Very Strong
   Time to crack: >1 Trillion Years
```
### Conclusion
- Simple passwords like name+number crack in seconds. 
- My final random password T!g3r$Un#9qL*2vX@8 takes trillions of years.
- So always use password manager.
###🔓 How Hackers Actually Crack Your Password in 4 Seconds – My Deep Dive | Task 6 | Elevate Labs

-I wanted to understand not just WHAT is a strong password, but HOW hackers break it. Here's what I learned:

1. DICTIONARY ATTACK – The 4-Second Hack
- Hackers have a list of 10 Million common passwords (sukanya, password, 123456).
- Their software tries 1 Lakh passwords per second.
- So if your password is "sukanya", it's cracked in 4 SECONDS.

2. BRUTE FORCE ATTACK – The 1-Month Hack
- Take "Sukanya124"
- Hackers know the pattern: Capital Letter + Name + Numbers.
- So they don't try all combinations, they only try: Sukanya + 000 to 999.
- That's just 1000 tries. Done in 1 month.

3. SOCIAL ENGINEERING – The Most Dangerous One
- This is what shocked me!
- I tested "Sukanya@2003" – I thought it was strong because it has a symbol.
- But the tool flagged: "Contains a date – Easily guessed"
- Why? A hacker checks your Instagram/Facebook, finds your DOB is 2003, and guesses it in the FIRST TRY.

4. WHY RANDOM IS UNBREAKABLE?
- My random password: "T!g3r$Un#9qL*2vX@8" – 16 characters
- 26 Capital + 26 Small + 10 Numbers + 32 Symbols = 94 options per character
- Total combinations = 94^16 = 37 Quintillion possibilities!
- Even a supercomputer needs 1 TRILLION years to crack it.

HACKER MINDSET:
- A hacker never attacks the hardest password. He attacks the easiest person.
- If you use an easy password, YOU become the target.

FINAL RULE I LEARNED:
- Don't create a password that YOU can remember.
- Create a password that even YOU cannot remember, and save it in a Password Manager.

