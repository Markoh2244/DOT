# Sample Test — What to Expect

Based on HackerRank / CodeSignal prep guides and candidate reports on Reddit
(r/leetcode, r/cscareerquestions, r/cpp), the common shape of a multi-language
(TypeScript / Python / Java / C++) quiz is:

| Section | Count | Time | Notes |
|---|---|---|---|
| A. Multiple choice | 6–10 | ~10 min | complexity, data structures, language basics |
| B. Predict the output | 4–6 | ~8 min | short snippets in your chosen language |
| C. Debug a snippet | 1 | ~7 min | find/fix an off-by-one or edge case |
| D. Coding problems | 2–4 | 30–60 min | Q1–Q2 easy, Q3 matrix/simulation, Q4 hash-map optimization |

Hidden tests check edge cases: empty input, single element, duplicates, negatives.
Answer key at the bottom. Time yourself: **~75 min total**.

---

## Section A — Multiple choice (pick one)

**A1.** Average-case lookup in a hash map (`dict`, `Map`, `HashMap`, `unordered_map`) is:
a) O(n)  b) O(log n)  c) O(1)  d) O(n log n)

**A2.** Which data structure gives LIFO (last-in, first-out) behavior?
a) Queue  b) Stack  c) Hash map  d) Linked list

**A3.** Time complexity of a good general-purpose sort (`sorted`, `Arrays.sort`, `std::sort`):
a) O(n)  b) O(n log n)  c) O(n²)  d) O(log n)

**A4.** Given `nums = [3, 1, 2]`, sorting ascending and returning the middle element gives:
a) 1  b) 2  c) 3  d) undefined

**A5.** Which loop runs exactly n times?
a) `for i in range(n)` / `for (let i = 0; i < n; i++)`
b) `for i in range(1, n)` / `for (let i = 1; i < n; i++)`
c) `while (n) {}` with no decrement
d) `for i in range(n + 1)`

**A6.** Two nested loops over an array of length n is typically:
a) O(n)  b) O(2n)  c) O(n²)  d) O(log n)

**A7.** What does integer division `7 / 2` give in Java and C++ (both `int`)?
a) 3.5  b) 3  c) 4  d) error

**A8.** In Python, `7 / 2` and `7 // 2` give respectively:
a) 3, 3  b) 3.5, 3  c) 3.5, 3.5  d) 3, 3.5

**A9.** Checking whether two strings have identical content — which is wrong?
a) Python `a == b`  b) TS `a === b`  c) Java `a == b`  d) C++ `a == b`

**A10.** Best structure to count how many times each word appears:
a) array  b) hash map  c) stack  d) set

---

## Section B — Predict the output

Answer in **your chosen language** (only that column is required).

| # | Python | TypeScript | Java | C++ |
|---|---|---|---|---|
| B1 | `print(len("hello"))` | `console.log("hello".length)` | `System.out.println("hello".length());` | `cout << string("hello").size();` |
| B2 | `print([1,2,3][-1])` | `console.log([1,2,3].at(-1))` | `int[] a={1,2,3}; System.out.println(a[a.length-1]);` | `vector<int> v{1,2,3}; cout << v.back();` |
| B3 | `print(10 % 3)` | `console.log(10 % 3)` | `System.out.println(10 % 3);` | `cout << 10 % 3;` |
| B4 | `print("ab" * 2)` | `console.log("ab".repeat(2))` | `System.out.println("ab".repeat(2));` | `cout << string("ab") + "ab";` |
| B5 | `print(sorted([3,1,2]))` | `console.log([3,1,2].sort((a,b)=>a-b))` | `int[] a={3,1,2}; Arrays.sort(a); System.out.println(Arrays.toString(a));` | `vector<int> v{3,1,2}; sort(v.begin(),v.end()); for(int x:v) cout<<x;` |
| B6 | `d={}; d['a']=d.get('a',0)+1; d['a']=d.get('a',0)+1; print(d)` | `const m=new Map(); m.set('a',(m.get('a')??0)+1); m.set('a',(m.get('a')??0)+1); console.log(m.get('a'))` | `Map<String,Integer> m=new HashMap<>(); m.put("a",m.getOrDefault("a",0)+1); m.put("a",m.getOrDefault("a",0)+1); System.out.println(m.get("a"));` | `unordered_map<char,int> m; m['a']++; m['a']++; cout << m['a'];` |

---

## Section C — Debug the snippet

The function should return the **sum of all elements**. It returns the wrong value. Find and fix the bug.

```python
def total(nums):
    s = 0
    for i in range(1, len(nums)):
        s += nums[i]
    return s
```

```ts
function total(nums: number[]): number {
  let s = 0;
  for (let i = 1; i < nums.length; i++) s += nums[i];
  return s;
}
```

```java
int total(int[] nums) {
    int s = 0;
    for (int i = 1; i < nums.length; i++) s += nums[i];
    return s;
}
```

```cpp
int total(const vector<int>& v) {
    int s = 0;
    for (size_t i = 1; i < v.size(); i++) s += v[i];
    return s;
}
```

---

## Section D — Coding problems

Write a complete function in your chosen language. Handle edge cases.

### D1 (Easy) — Count Vowels
Given a string `s`, return how many characters are vowels (`a e i o u`, case-insensitive).
- `"Hello World"` → `3`
- `""` → `0`

### D2 (Easy) — First Duplicate
Given an int array, return the first value that appears a second time when scanning left to right. Return `-1` if none.
- `[2, 1, 3, 5, 3, 2]` → `3`
- `[1, 2, 3]` → `-1`

### D3 (Medium, matrix) — Count Islands of 1s
Given a grid of `0`/`1`, count the number of connected groups of `1`s (4-directional).
```
1 1 0
0 1 0
0 0 1
```
→ `2`

### D4 (Medium, hash map) — Longest Substring Without Repeating Characters
Return the length of the longest substring of `s` with all distinct characters.
- `"abcabcbb"` → `3` (`"abc"`)
- `"bbbb"` → `1`
- `""` → `0`

---

## Answer key

**Section A:** A1 c · A2 b · A3 b · A4 b · A5 a · A6 c · A7 b · A8 b · A9 c (Java `==` compares references; use `.equals`) · A10 b

**Section B:** B1 `5` · B2 `3` · B3 `1` · B4 `abab` · B5 `[1, 2, 3]` / `123` in C++ · B6 `2` (Python prints `{'a': 2}`)

**Section C:** Loop starts at index 1 and skips the first element. Start at `0`.

**Section D (Python reference; translate the idea to your language):**

```python
def count_vowels(s):
    return sum(c in "aeiou" for c in s.lower())

def first_duplicate(nums):
    seen = set()
    for x in nums:
        if x in seen:
            return x
        seen.add(x)
    return -1

def count_islands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    seen = [[False] * cols for _ in range(rows)]

    def flood(r, c):
        stack = [(r, c)]
        while stack:
            i, j = stack.pop()
            if 0 <= i < rows and 0 <= j < cols and grid[i][j] == 1 and not seen[i][j]:
                seen[i][j] = True
                stack += [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and not seen[r][c]:
                flood(r, c)
                count += 1
    return count

def longest_unique(s):
    last = {}
    start = best = 0
    for i, ch in enumerate(s):
        if ch in last and last[ch] >= start:
            start = last[ch] + 1
        last[ch] = i
        best = max(best, i - start + 1)
    return best
```

**Complexities:** D1 O(n) · D2 O(n) with a set · D3 O(rows·cols) · D4 O(n) sliding window.

---

## Scoring yourself

- A + B: aim for **≥ 80%**. Below that → drill `cheatsheets/<lang>.md` and `python3 practice.py <lang>`.
- C: should take under 3 minutes.
- D1–D2: must be clean and fast (≤ 10 min each). D3–D4: partial credit is normal; pattern recognition (flood fill, sliding window) is what to practice.
