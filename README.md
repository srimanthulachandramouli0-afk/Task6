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
