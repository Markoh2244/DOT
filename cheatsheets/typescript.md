# TypeScript quiz cheatsheet

## Arrays
```ts
const a: number[] = [1, 2, 3];
a.push(4); a.pop();
a.map(x => x * 2);
a.filter(x => x > 1);
a.reduce((s, x) => s + x, 0);
a.includes(2);
[...a]; a.slice();          // shallow copy
a.sort((x, y) => x - y);    // numeric sort
```

## Strings
```ts
s.length; s[i]; s.slice(i, j);
s.split(' '); s.split(/\s+/);
s.includes('ab'); s.startsWith('a');
s.toLowerCase(); [...s];    // chars
```

## Map / object counts
```ts
const m = new Map<string, number>();
m.set(k, (m.get(k) ?? 0) + 1);
m.has(k); m.get(k);

const o: Record<string, number> = {};
o[k] = (o[k] ?? 0) + 1;
Object.keys(o); Object.entries(o);
```

## Set
```ts
const set = new Set(arr);
set.add(x); set.has(x); [...set];
```

## Types to remember
`number[]`, `string`, `boolean`, `Record<string, number>`, `Map<K,V>`, `() => void`, `x?: number`
