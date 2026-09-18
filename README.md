# Language Quiz Coach

Find which language you're strongest in (**TypeScript**, **Python**, **Java**, or **C++**), then practice that language until you're quiz-ready.

## Quick start

```bash
python3 take-diagnostic.py
```

The diagnostic:

1. Asks the **same coding tasks** in all four languages (you answer in whichever you know).
2. Asks **language-specific** multiple-choice questions.
3. Scores you and **recommends one language**.
4. Points you to a focused practice set.

## Practice after the diagnostic

```bash
# After you get a recommendation, e.g. python:
python3 practice.py python

# Or pick any language:
python3 practice.py typescript
python3 practice.py java
python3 practice.py cpp
```

## What's included

| Path | Purpose |
|------|---------|
| `take-diagnostic.py` | Interactive placement quiz + recommendation |
| `practice.py` | Interactive practice drills for one language |
| `practice/` | Problem statements, starter code, and solutions |
| `cheatsheets/` | Quick syntax refreshers for quiz day |

## Tips for quiz success

- Prefer the language where you can write correct code **fast**, not the one that feels fanciest.
- If scores are close, pick the language with the fewest "blank stare" moments on syntax.
- Drill: arrays/lists, maps/dicts, strings, loops, recursion, and common library APIs.
