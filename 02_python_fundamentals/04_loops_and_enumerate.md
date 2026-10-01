# 04 — Loops and enumerate()

A `for` loop repeats an operation for each item.

```python
frutti = ["mela", "pera", "banana"]

for frutto in frutti:
    print(frutto)
```

When both index and value are needed:

```python
for i, frutto in enumerate(frutti):
    print(i, frutto)
```

## Key Takeaway

Use `for` to iterate over data. Use `enumerate()` when you need both position and value.
