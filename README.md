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
