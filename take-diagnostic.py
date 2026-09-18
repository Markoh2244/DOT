#!/usr/bin/env python3
"""
Interactive diagnostic: discover which of TypeScript / Python / Java / C++
you should take a programming quiz in.
"""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass, field
from pathlib import Path

LANGS = ("typescript", "python", "java", "cpp")
LANG_LABEL = {
    "typescript": "TypeScript",
    "python": "Python",
    "java": "Java",
    "cpp": "C++",
}


@dataclass
class Scores:
    knowledge: dict[str, int] = field(default_factory=lambda: {l: 0 for l in LANGS})
    coding_comfort: dict[str, int] = field(default_factory=lambda: {l: 0 for l in LANGS})
    self_speed: dict[str, int] = field(default_factory=lambda: {l: 0 for l in LANGS})
    knowledge_max: dict[str, int] = field(default_factory=lambda: {l: 0 for l in LANGS})

    def total(self, lang: str) -> float:
        # Weighted: knowledge 50%, coding comfort 30%, self-reported speed 20%
        kmax = max(self.knowledge_max[lang], 1)
        k = self.knowledge[lang] / kmax
        c = self.coding_comfort[lang] / 5.0
        s = self.self_speed[lang] / 5.0
        return 100.0 * (0.5 * k + 0.3 * c + 0.2 * s)


def banner(title: str) -> None:
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def ask(prompt: str) -> str:
    try:
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        print("\nExiting.")
        sys.exit(0)


def ask_choice(prompt: str, options: dict[str, str]) -> str:
    print(prompt)
    for key, label in options.items():
        print(f"  {key}) {label}")
    while True:
        ans = ask("Your answer: ").lower()
        if ans in options:
            return ans
        print(f"Please enter one of: {', '.join(options)}")


def ask_scale(prompt: str) -> int:
    print(prompt)
    print("  1 = not at all   …   5 = very confident / fast")
    while True:
        ans = ask("Rating (1-5): ")
        if ans in {"1", "2", "3", "4", "5"}:
            return int(ans)
        print("Enter a number from 1 to 5.")


# --- Knowledge questions (language-specific) ---

KNOWLEDGE = {
    "typescript": [
        {
            "q": "What does `const xs: number[] = [1, 2, 3]; xs.map(x => x * 2)` return?",
            "options": {"a": "[1, 2, 3]", "b": "[2, 4, 6]", "c": "undefined", "d": "a Map"},
            "answer": "b",
        },
        {
            "q": "Which checks both value AND type?",
            "options": {"a": "==", "b": "=", "c": "===", "d": "!==="},
            "answer": "c",
        },
        {
            "q": "How do you declare an optional property `age` on an interface?",
            "options": {
                "a": "age?: number",
                "b": "age: number?",
                "c": "optional age: number",
                "d": "age: number | void",
            },
            "answer": "a",
        },
        {
            "q": "What is the result of `[...new Set([1, 1, 2, 3])]`?",
            "options": {"a": "[1, 1, 2, 3]", "b": "[1, 2, 3]", "c": "Set(3)", "d": "error"},
            "answer": "b",
        },
        {
            "q": "Which correctly types a function that returns nothing useful?",
            "options": {
                "a": "function f(): null {}",
                "b": "function f(): void {}",
                "c": "function f(): undefined {}",
                "d": "function f(): never {}",
            },
            "answer": "b",
        },
    ],
    "python": [
        {
            "q": "What does `[x * 2 for x in [1, 2, 3]]` produce?",
            "options": {"a": "[1, 2, 3]", "b": "[2, 4, 6]", "c": "(2, 4, 6)", "d": "{2, 4, 6}"},
            "answer": "b",
        },
        {
            "q": "What is the time complexity of average dict lookup by key?",
            "options": {"a": "O(n)", "b": "O(log n)", "c": "O(1)", "d": "O(n log n)"},
            "answer": "c",
        },
        {
            "q": "What does `\"a,b,c\".split(\",\")` return?",
            "options": {"a": "('a','b','c')", "b": "['a','b','c']", "c": "'a b c'", "d": "error"},
            "answer": "b",
        },
        {
            "q": "Which creates a shallow copy of list `xs`?",
            "options": {"a": "xs", "b": "xs.copy()", "c": "list = xs", "d": "xs.deepcopy()"},
            "answer": "b",
        },
        {
            "q": "What does `sorted([3, 1, 2], reverse=True)` return?",
            "options": {"a": "[1, 2, 3]", "b": "[3, 2, 1]", "c": "None", "d": "[3, 1, 2]"},
            "answer": "b",
        },
    ],
    "java": [
        {
            "q": "Which creates an ArrayList of Integers?",
            "options": {
                "a": "List<int> a = new ArrayList<>();",
                "b": "List<Integer> a = new ArrayList<>();",
                "c": "ArrayList a = List<>();",
                "d": "int[] a = new ArrayList<>();",
            },
            "answer": "b",
        },
        {
            "q": "How do you compare two strings `s1` and `s2` for equal content?",
            "options": {"a": "s1 == s2", "b": "s1.equals(s2)", "c": "s1.compare(s2)", "d": "equals(s1, s2)"},
            "answer": "b",
        },
        {
            "q": "What does `map.getOrDefault(k, 0)` do if key is missing?",
            "options": {"a": "returns null", "b": "throws", "c": "returns 0", "d": "inserts 0"},
            "answer": "c",
        },
        {
            "q": "Which loop variable scope is valid in modern Java enhanced-for?",
            "options": {
                "a": "for (int x : arr) { }",
                "b": "for (x in arr) { }",
                "c": "for each (int x in arr)",
                "d": "foreach (arr as x)",
            },
            "answer": "a",
        },
        {
            "q": "String concatenation in a tight loop is best done with:",
            "options": {
                "a": "str = str + x",
                "b": "StringBuilder",
                "c": "StringBuffer only",
                "d": "String.join always",
            },
            "answer": "b",
        },
    ],
    "cpp": [
        {
            "q": "Which includes the dynamic array container?",
            "options": {"a": "#include <array>", "b": "#include <vector>", "c": "#include <list>", "d": "#include <dyn>"},
            "answer": "b",
        },
        {
            "q": "How do you get the number of elements in `vector<int> v`?",
            "options": {"a": "v.length()", "b": "v.size()", "c": "len(v)", "d": "sizeof(v)"},
            "answer": "b",
        },
        {
            "q": "What does `unordered_map` average lookup complexity?",
            "options": {"a": "O(n)", "b": "O(log n)", "c": "O(1)", "d": "O(n^2)"},
            "answer": "c",
        },
        {
            "q": "Which passes an int vector without copying?",
            "options": {
                "a": "void f(vector<int> v)",
                "b": "void f(vector<int>& v)",
                "c": "void f(vector<int>* v) only",
                "d": "void f(auto v)",
            },
            "answer": "b",
        },
        {
            "q": "Range-based for over a vector `v`:",
            "options": {
                "a": "for (int x : v) {}",
                "b": "for x in v {}",
                "c": "foreach (x : v)",
                "d": "for (int x <<= v)",
            },
            "answer": "a",
        },
    ],
}


CODING_TASKS = [
    {
        "id": "two_sum",
        "title": "Two Sum indices",
        "prompt": (
            "Given an array of ints and a target, return two indices i < j such that\n"
            "nums[i] + nums[j] == target. Assume exactly one solution.\n"
            "Example: nums=[2,7,11,15], target=9 -> [0,1]"
        ),
    },
    {
        "id": "freq",
        "title": "Character frequency",
        "prompt": (
            "Given a string s, return a map/dict from each character to how often it appears.\n"
            "Example: \"aab\" -> {'a': 2, 'b': 1}"
        ),
    },
    {
        "id": "reverse_words",
        "title": "Reverse words",
        "prompt": (
            "Reverse the order of words in a sentence (words split on spaces).\n"
            "Example: \"hello world quiz\" -> \"quiz world hello\""
        ),
    },
]


def run_self_assessment(scores: Scores) -> None:
    banner("PART 1 — Self assessment (honest = better recommendation)")
    print(
        "For each language, rate how FAST you could solve a typical coding-quiz\n"
        "problem (arrays, strings, maps, loops) without docs."
    )
    for lang in LANGS:
        scores.self_speed[lang] = ask_scale(f"\n{LANG_LABEL[lang]} — quiz speed/comfort:")


def run_knowledge(scores: Scores) -> None:
    banner("PART 2 — Knowledge check (5 questions per language)")
    print("Answer even if guessing — leave blank only if you truly have no idea.")
    for lang in LANGS:
        print(f"\n--- {LANG_LABEL[lang]} ---")
        questions = KNOWLEDGE[lang]
        scores.knowledge_max[lang] = len(questions)
        for i, item in enumerate(questions, 1):
            print(f"\nQ{i}. {item['q']}")
            choice = ask_choice("", item["options"])
            if choice == item["answer"]:
                scores.knowledge[lang] += 1
                print("  ✓ correct")
            else:
                print(f"  ✗ correct was ({item['answer']}) {item['options'][item['answer']]}")


def run_coding_comfort(scores: Scores) -> None:
    banner("PART 3 — Coding comfort (same 3 tasks, all languages)")
    print(
        "You do NOT need to write full code here.\n"
        "For each task + language, rate: could you code a correct solution in ~5–10 minutes?"
    )
    for task in CODING_TASKS:
        print(f"\n### Task: {task['title']}")
        print(task["prompt"])
        for lang in LANGS:
            rating = ask_scale(f"\nCould you implement this quickly in {LANG_LABEL[lang]}?")
            scores.coding_comfort[lang] += rating
    # Normalize comfort to 0–5 average later via /5 in total(); we summed 3 ratings of 1–5
    # So divide by 3 to keep 1–5 scale
    for lang in LANGS:
        scores.coding_comfort[lang] = round(scores.coding_comfort[lang] / len(CODING_TASKS))


def recommend(scores: Scores) -> str:
    ranked = sorted(LANGS, key=lambda l: scores.total(l), reverse=True)
    return ranked[0]


def print_report(scores: Scores, best: str) -> None:
    banner("RESULTS")
    rows = []
    for lang in LANGS:
        rows.append((scores.total(lang), lang))
    rows.sort(reverse=True)

    print(f"{'Language':<14} {'Score':>7}  {'Knowledge':>10}  {'Comfort':>8}  {'Speed':>6}")
    print("-" * 55)
    for total, lang in rows:
        k = f"{scores.knowledge[lang]}/{scores.knowledge_max[lang]}"
        print(
            f"{LANG_LABEL[lang]:<14} {total:6.1f}%  {k:>10}  "
            f"{scores.coding_comfort[lang]:>7}/5  {scores.self_speed[lang]:>5}/5"
        )

    print("\n" + "*" * 60)
    print(f"  RECOMMENDATION: Take the quiz in {LANG_LABEL[best]}!")
    print("*" * 60)
    second = rows[1][1]
    gap = rows[0][0] - rows[1][0]
    if gap < 8:
        print(
            f"\nClose call with {LANG_LABEL[second]} (only {gap:.1f} points behind).\n"
            f"If you feel more natural typing {LANG_LABEL[second]}, that is fine too."
        )

    print(
        f"\nNext step — practice in {LANG_LABEL[best]}:\n"
        f"  python3 practice.py {best}\n\n"
        f"Cheat sheet:\n"
        f"  cheatsheets/{best}.md"
    )

    out = Path("diagnostic-result.json")
    payload = {
        "recommendation": best,
        "scores": {
            lang: {
                "total": round(scores.total(lang), 1),
                "knowledge": scores.knowledge[lang],
                "knowledge_max": scores.knowledge_max[lang],
                "coding_comfort": scores.coding_comfort[lang],
                "self_speed": scores.self_speed[lang],
            }
            for lang in LANGS
        },
    }
    out.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"\nSaved detailed result to {out}")


def main() -> None:
    banner("Language Placement Diagnostic")
    print(
        "Goal: pick ONE language for your quiz among TypeScript, Python, Java, C++.\n"
        "Answer honestly — this takes about 10–15 minutes."
    )
    ready = ask("\nPress Enter to start (or q to quit): ").lower()
    if ready == "q":
        return

    scores = Scores()
    run_self_assessment(scores)
    run_knowledge(scores)
    run_coding_comfort(scores)
    best = recommend(scores)
    print_report(scores, best)


if __name__ == "__main__":
    main()
