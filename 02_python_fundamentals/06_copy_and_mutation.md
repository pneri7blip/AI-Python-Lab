# 06 — Copying and Mutation

Lists are mutable.

```python
numeri = [1, 2, 3]
numeri.append(4)
```

The original list changes.

To create an independent copy:

```python
numeri = [1, 2, 3]
copia = numeri.copy()
copia.append(4)
```

Now the original remains unchanged.

## Key Takeaway

`.copy()` creates an independent list, so changes to the copy do not modify the original list.
