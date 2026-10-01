# 07 — Scope and Common Errors

Variables created inside a function normally belong to that function.

```python
def calcola(prezzo):
    sconto = prezzo * 0.20
    return prezzo - sconto
```

`sconto` is local to `calcola()`.

A function without `return` returns `None`.

## Key Takeaway

Always pay attention to where a variable is created and whether a function actually returns a value.
