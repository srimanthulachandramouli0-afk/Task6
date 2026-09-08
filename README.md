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

File: Checker.py
import re

def check(p):
    s = 0
    if len(p) >= 8: s+=1
    if len(p) >= 12: s+=1
    if re.search(r"[A-Z]", p): s+=1
    if re.search(r"[a-z]", p): s+=1
    if re.search(r"[0-9]", p): s+=1
    if re.search(r"[^a-zA-Z0-9]", p): s+=1
    
    if s <= 2:
        return "Very Weak"
    elif s <= 4:
        return "Medium"
    else:
        return "Very Strong - 100%"

for pwd in ["password", "Password123", "T!g3r$Un#9qL*2vX@8"]:
    print(pwd, "->", check(pwd))

