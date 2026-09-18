# Python quiz cheatsheet

## Lists
```python
a = [1, 2, 3]
a.append(4); a.pop()
a[0]; a[-1]; a[1:3]
sorted(a); a.sort()
[x * 2 for x in a]
list(enumerate(a))  # (i, val)
```

## Strings
```python
s.split()           # collapse whitespace
' '.join(parts)
s.lower(); s[::-1]  # reverse
s.count('a'); c in s
```

## Dict counts
```python
d = {}
d[k] = d.get(k, 0) + 1
from collections import Counter, defaultdict
Counter('aab')
dd = defaultdict(int); dd[k] += 1
```

## Set
```python
s = set(a); s.add(x); x in s
s | t; s & t; s - t
```

## Handy
```python
range(n); range(1, n+1)
zip(a, b); any(...); all(...)
float('inf')
```
