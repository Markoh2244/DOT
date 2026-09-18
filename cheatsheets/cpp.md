# C++ quiz cheatsheet

## Includes
```cpp
#include <bits/stdc++.h>   // if allowed
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>
using namespace std;
```

## vector / string
```cpp
vector<int> v; v.push_back(x); v.size(); v.back();
sort(v.begin(), v.end());
string s; s.size(); s[i]; s += 'a';
```

## unordered_map counts
```cpp
unordered_map<char, int> m;
m[c]++;                 // default 0
m.count(c); m[c];
for (auto& [k, val] : m) { }
```

## set
```cpp
unordered_set<int> s; s.insert(x); s.count(x);
```

## Pass big objects
```cpp
void f(const vector<int>& v);  // no copy
```

## Remember
- `size()` is `size_t` (unsigned)
- `==` works for `string` content
- Prefer `unordered_map` for O(1) avg lookups
