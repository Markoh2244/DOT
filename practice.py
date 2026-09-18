#!/usr/bin/env python3
"""Interactive practice coach for TypeScript, Python, Java, or C++."""

from __future__ import annotations

import json
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PRACTICE = ROOT / "practice"

LANG_LABEL = {
    "typescript": "TypeScript",
    "python": "Python",
    "java": "Java",
    "cpp": "C++",
}

# Multiple-choice drills: concept + syntax that trip people up on quizzes
MCQ = {
    "typescript": [
        {
            "q": "Pick the correctly typed optional callback:",
            "options": {
                "a": "onDone?: () => void",
                "b": "onDone: () => void?",
                "c": "onDone: optional void()",
                "d": "onDone?: void => ()",
            },
            "answer": "a",
            "explain": "Optional props use `name?: type`. Function type is `() => void`.",
        },
        {
            "q": "What does `array.filter(Boolean)` do on `[0, 1, '', 'x', null]`?",
            "options": {
                "a": "keeps only truthy values → [1, 'x']",
                "b": "converts all to boolean",
                "c": "removes only null",
                "d": "throws a type error always",
            },
            "answer": "a",
            "explain": "Boolean as callback removes falsy values (0, '', null, undefined, false).",
        },
        {
            "q": "Best way to clone a shallow array `a`?",
            "options": {"a": "a", "b": "[...a]", "c": "a.clone()", "d": "Array.copy(a)"},
            "answer": "b",
            "explain": "Spread `[...a]` or `a.slice()` makes a shallow copy.",
        },
        {
            "q": "`Object.keys({a:1,b:2})` returns:",
            "options": {"a": "['a','b']", "b": "[1,2]", "c": "[['a',1],['b',2]]", "d": "Set"},
            "answer": "a",
            "explain": "Object.keys returns string keys.",
        },
        {
            "q": "Which Map usage is correct?",
            "options": {
                "a": "const m = new Map(); m.set('a', 1); m.get('a')",
                "b": "const m = Map(); m['a']=1",
                "c": "const m = {}; m.set('a',1)",
                "d": "Map.of('a',1).get",
            },
            "answer": "a",
            "explain": "Use Map methods set/get/has, not plain object bracket assignment on Map.",
        },
        {
            "q": "Result of `'hi'.repeat(3)`?",
            "options": {"a": "'hihihi'", "b": "['hi','hi','hi']", "c": "error", "d": "'hi3'"},
            "answer": "a",
            "explain": "String.repeat concatenates the string n times.",
        },
        {
            "q": "Type for a dictionary of string→number?",
            "options": {
                "a": "Record<string, number>",
                "b": "Dict<string, number>",
                "c": "Map<string>()",
                "d": "object<number>",
            },
            "answer": "a",
            "explain": "Record<K,V> or `{ [key: string]: number }` are common.",
        },
        {
            "q": "`nums.reduce((a,b)=>a+b, 0)` on `[1,2,3]` is:",
            "options": {"a": "6", "b": "0", "c": "[1,2,3]", "d": "undefined"},
            "answer": "a",
            "explain": "reduce with initial 0 sums the array.",
        },
    ],
    "python": [
        {
            "q": "`d = {}; d['a'] = d.get('a', 0) + 1` after one run — d is:",
            "options": {"a": "{'a': 1}", "b": "{'a': 0}", "c": "{}", "d": "error"},
            "answer": "a",
            "explain": "Classic frequency counter pattern with dict.get default.",
        },
        {
            "q": "What does `list(enumerate(['a','b']))` produce?",
            "options": {
                "a": "[(0,'a'),(1,'b')]",
                "b": "['a','b']",
                "c": "[0,1]",
                "d": "{0:'a',1:'b'}",
            },
            "answer": "a",
            "explain": "enumerate yields (index, value) pairs.",
        },
        {
            "q": "`''.join(['a','b','c'])` →",
            "options": {"a": "'abc'", "b": "'a b c'", "c": "['abc']", "d": "error"},
            "answer": "a",
            "explain": "join concatenates with the separator (here empty string).",
        },
        {
            "q": "Which is a set literal?",
            "options": {"a": "{}", "b": "{1, 2, 3}", "c": "set[]", "d": "[1,2,3]"},
            "answer": "b",
            "explain": "`{}` is an empty dict; nonempty `{1,2}` is a set. Empty set is `set()`.",
        },
        {
            "q": "`sorted('cab')` returns:",
            "options": {"a": "['a','b','c']", "b": "'abc'", "c": "('a','b','c')", "d": "'cab'"},
            "answer": "a",
            "explain": "sorted always returns a new list.",
        },
        {
            "q": "Default mutable arg pitfall — which is safest?",
            "options": {
                "a": "def f(xs=[]):",
                "b": "def f(xs=None):\n    if xs is None: xs = []",
                "c": "def f(xs=list):",
                "d": "def f(xs={}):",
            },
            "answer": "b",
            "explain": "Never use mutable default args; use None sentinel.",
        },
        {
            "q": "`[1,2,3][-1]` is:",
            "options": {"a": "1", "b": "2", "c": "3", "d": "error"},
            "answer": "c",
            "explain": "Negative indices count from the end.",
        },
        {
            "q": "`collections.Counter('aab')['a']` is:",
            "options": {"a": "2", "b": "1", "c": "0", "d": "['a','a']"},
            "answer": "a",
            "explain": "Counter counts hashable items; 'a' appears twice.",
        },
    ],
    "java": [
        {
            "q": "Correct HashMap declaration?",
            "options": {
                "a": "Map<String, Integer> m = new HashMap<>();",
                "b": "HashMap m = Map<String, Integer>();",
                "c": "dict<String,Integer> m = new HashMap();",
                "d": "Map m = new Map<>();",
            },
            "answer": "a",
            "explain": "Program to Map interface; construct HashMap with diamond <> .",
        },
        {
            "q": "Increment count for key in map:",
            "options": {
                "a": "m.put(k, m.getOrDefault(k, 0) + 1);",
                "b": "m[k]++",
                "c": "m.add(k,1)",
                "d": "m.get(k) += 1 always safe",
            },
            "answer": "a",
            "explain": "getOrDefault avoids null; put writes back.",
        },
        {
            "q": "`\"ab\".charAt(1)` returns:",
            "options": {"a": "'a'", "b": "'b'", "c": "1", "d": "\"b\""},
            "answer": "b",
            "explain": "charAt returns char; index 1 is second character.",
        },
        {
            "q": "Convert ArrayList<Integer> to array?",
            "options": {
                "a": "list.toArray(new Integer[0])",
                "b": "list.array()",
                "c": "(Integer[]) list",
                "d": "Arrays.of(list)",
            },
            "answer": "a",
            "explain": "toArray with typed empty array is the idiomatic approach.",
        },
        {
            "q": "Strings are compared with == when:",
            "options": {
                "a": "you want content equality",
                "b": "you want reference identity (usually wrong for content)",
                "c": "always identical to equals",
                "d": "for null-safe content check",
            },
            "answer": "b",
            "explain": "Use equals (or Objects.equals) for content.",
        },
        {
            "q": "`Arrays.sort(arr)` on int[]:",
            "options": {
                "a": "sorts ascending in place",
                "b": "returns new sorted array",
                "c": "only works on Integer[]",
                "d": "sorts descending",
            },
            "answer": "a",
            "explain": "Arrays.sort mutates the array ascending.",
        },
        {
            "q": "Boxing: which compiles?",
            "options": {
                "a": "List<int> x = new ArrayList<>();",
                "b": "List<Integer> x = new ArrayList<>();",
                "c": "List<Int> x = new ArrayList<>();",
                "d": "ArrayList<int> x = new ArrayList<int>();",
            },
            "answer": "b",
            "explain": "Generics need reference types (Integer), not primitives (int).",
        },
        {
            "q": "Read length of String s / array a:",
            "options": {
                "a": "s.length() and a.length",
                "b": "s.length and a.length()",
                "c": "s.size() and a.size()",
                "d": "len(s) and len(a)",
            },
            "answer": "a",
            "explain": "String: length(); array: length field; Collection: size().",
        },
    ],
    "cpp": [
        {
            "q": "Include + use a hash map of string→int:",
            "options": {
                "a": "#include <unordered_map> then unordered_map<string,int> m;",
                "b": "#include <map> then HashMap m;",
                "c": "#include <dict>",
                "d": "using map = hash;",
            },
            "answer": "a",
            "explain": "unordered_map is the usual hash table; map is ordered tree map.",
        },
        {
            "q": "`v.push_back(3)` on vector<int> v does:",
            "options": {
                "a": "appends 3",
                "b": "inserts at front",
                "c": "sets v[0]=3",
                "d": "returns new vector",
            },
            "answer": "a",
            "explain": "push_back appends; emplace_back constructs in place.",
        },
        {
            "q": "Iterate keys of unordered_map<string,int> m:",
            "options": {
                "a": "for (auto& [k,v] : m) {}",
                "b": "for (k in m.keys)",
                "c": "m.forEach",
                "d": "for (int i=0;i<m;i++)",
            },
            "answer": "a",
            "explain": "C++17 structured bindings work well with maps.",
        },
        {
            "q": "Prefer for read-only pass of big vector:",
            "options": {
                "a": "void f(vector<int> v)",
                "b": "void f(const vector<int>& v)",
                "c": "void f(vector<int>&& v) always",
                "d": "void f(vector<int>* v) only",
            },
            "answer": "b",
            "explain": "const reference avoids copy and prevents mutation.",
        },
        {
            "q": "`string s = \"hi\"; s.size();` type of size?",
            "options": {"a": "int always", "b": "size_t", "c": "long", "d": "char"},
            "answer": "b",
            "explain": "size()/length() return size_t (unsigned).",
        },
        {
            "q": "Sort vector ascending:",
            "options": {
                "a": "sort(v.begin(), v.end());",
                "b": "v.sort();",
                "c": "sorted(v);",
                "d": "Arrays.sort(v);",
            },
            "answer": "a",
            "explain": "Need #include <algorithm> and iterators.",
        },
        {
            "q": "Avoid dangling — which is safest return?",
            "options": {
                "a": "return reference to local vector",
                "b": "return vector by value (NRVO/move)",
                "c": "return pointer to local int",
                "d": "return &local_string",
            },
            "answer": "b",
            "explain": "Return by value; locals are destroyed when function ends.",
        },
        {
            "q": "`v.back()` on nonempty vector:",
            "options": {
                "a": "last element",
                "b": "first element",
                "c": "size",
                "d": "iterator to end",
            },
            "answer": "a",
            "explain": "back() is the last element; front() is the first.",
        },
    ],
}


def load_coding_problems(lang: str) -> list[dict]:
    path = PRACTICE / lang / "problems.json"
    return json.loads(path.read_text())


def ask(prompt: str) -> str:
    try:
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        print("\nBye!")
        sys.exit(0)


def ask_mcq(item: dict) -> bool:
    print("\n" + item["q"])
    for k, v in item["options"].items():
        # show first line only for multi-line options
        first = v.split("\n")[0]
        print(f"  {k}) {first}")
        for extra in v.split("\n")[1:]:
            print(f"       {extra}")
    while True:
        ans = ask("Your answer: ").lower()
        if ans in item["options"]:
            break
        print("Pick one of:", ", ".join(item["options"]))
    ok = ans == item["answer"]
    if ok:
        print("✓ Correct!", item["explain"])
    else:
        print(f"✗ Nope. Answer was ({item['answer']}). {item['explain']}")
    return ok


def run_mcq_round(lang: str, n: int = 8) -> tuple[int, int]:
    items = MCQ[lang][:]
    random.shuffle(items)
    items = items[:n]
    correct = 0
    for i, item in enumerate(items, 1):
        print(f"\n--- MCQ {i}/{len(items)} ---")
        if ask_mcq(item):
            correct += 1
    return correct, len(items)


def run_coding_round(lang: str) -> None:
    problems = load_coding_problems(lang)
    print("\n" + "=" * 60)
    print("CODING DRILLS — read the problem, try on paper/IDE, then reveal")
    print("=" * 60)
    for i, p in enumerate(problems, 1):
        print(f"\n### Problem {i}: {p['title']}")
        print(p["prompt"])
        print(f"\nStarter ({LANG_LABEL[lang]}):\n")
        print(p["starter"])
        ask("\nPress Enter when you've attempted it (or skip)...")
        show = ask("Show solution? [Y/n]: ").lower()
        if show in ("", "y", "yes"):
            print("\n--- Solution ---")
            print(p["solution"])
            print("\n--- Why it works ---")
            print(p["explanation"])
        got = ask("Did you solve it (mostly) correctly? [y/n]: ").lower()
        p["_ok"] = got in ("y", "yes")
    solved = sum(1 for p in problems if p.get("_ok"))
    print(f"\nCoding self-score: {solved}/{len(problems)} marked correct.")


def main() -> None:
    if len(sys.argv) < 2 or sys.argv[1] not in LANG_LABEL:
        print("Usage: python3 practice.py <typescript|python|java|cpp>")
        # If diagnostic result exists, hint
        result = ROOT / "diagnostic-result.json"
        if result.exists():
            data = json.loads(result.read_text())
            rec = data.get("recommendation")
            if rec:
                print(f"Diagnostic recommended: {rec}")
                print(f"  python3 practice.py {rec}")
        sys.exit(1)

    lang = sys.argv[1]
    print("=" * 60)
    print(f"Practice mode: {LANG_LABEL[lang]}")
    print("=" * 60)
    print("1) Multiple-choice warm-up")
    print("2) Coding drills with solutions")
    print("3) Both")
    mode = ask("Choose 1/2/3: ")
    if mode not in {"1", "2", "3"}:
        mode = "3"

    if mode in {"1", "3"}:
        c, t = run_mcq_round(lang)
        print(f"\n*** MCQ score: {c}/{t} ({100*c//t}%) ***")
        if c / t < 0.7:
            print(f"Review cheatsheets/{lang}.md and retry MCQs.")
        else:
            print("Solid syntax recall — nice.")

    if mode in {"2", "3"}:
        run_coding_round(lang)

    print(
        f"\nQuiz-day checklist for {LANG_LABEL[lang]}:\n"
        f"  • Skim cheatsheets/{lang}.md\n"
        f"  • Re-run: python3 practice.py {lang}\n"
        f"  • Time yourself on the coding drills (10 min each)\n"
    )


if __name__ == "__main__":
    main()
