# Java quiz cheatsheet

## Lists / arrays
```java
List<Integer> list = new ArrayList<>();
list.add(x); list.get(i); list.size();
list.sort(null); Collections.sort(list);
int[] a = {1,2,3}; a.length; Arrays.sort(a);
```

## Strings
```java
s.length(); s.charAt(i); s.substring(i, j);
s.equals(t);  // NOT ==
s.split("\\s+"); String.join(" ", parts);
Integer.parseInt("12"); String.valueOf(n);
```

## Map counts
```java
Map<Character, Integer> m = new HashMap<>();
m.put(c, m.getOrDefault(c, 0) + 1);
m.containsKey(c); m.get(c);
for (var e : m.entrySet()) { e.getKey(); e.getValue(); }
```

## Set
```java
Set<Integer> set = new HashSet<>();
set.add(x); set.contains(x);
```

## Remember
- Generics: `Integer` not `int`
- `StringBuilder` for heavy concatenation
- `import java.util.*;`
