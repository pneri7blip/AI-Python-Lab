# 05 — Functions, Parameters, and return

A function groups reusable logic.

```python
def aggiungi(lista):
    lista.append("pera")
```

A function can return a value:

```python
def calcola_sconto(prezzo):
    sconto = prezzo * 0.20
    nuovo_prezzo = prezzo - sconto
    return nuovo_prezzo
```

Then:

```python
risultato = calcola_sconto(100)
```

`print()` displays something; `return` sends a value back to the code that called the function.

## Key Takeaway

Use `print()` to display; use `return` when the result must be used by other code.
