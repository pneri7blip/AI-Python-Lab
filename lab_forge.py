from pathlib import Path

FILES = {
"README_PYTHON_PORTFOLIO.md": """# Python & AI Portfolio

This section documents my practical Python learning path for AI and LLM work.

The goal is not to present myself as a professional Python developer, but to demonstrate that I can understand, explain, modify, and build small Python components used in AI workflows and APIs.

## Focus

- Python fundamentals
- Data structures and iteration
- Functions, parameters, and return values
- Mutation, copying, and scope
- Packages and `pip`
- JSON and APIs
- Reading AI API code
- Foundations for LLM applications

## Learning principle

I focus on understanding what the code is doing and why, rather than memorizing syntax without context.
""",

"02_python_fundamentals/README.md": """# Python Fundamentals

Practical Python foundations developed as part of my AI/LLM learning path.

## Topics

1. Variables and types
2. Lists and methods
3. Dictionaries and nested data
4. Loops and `enumerate()`
5. Functions, parameters, and `return`
6. Copying and mutation
7. Scope and common errors
8. Randomness and input logic
9. Packages, pip, JSON, and APIs
10. Reading AI API code
""",

"02_python_fundamentals/01_variables_and_types.md": """# 01 — Variables and Types

## Core concepts

Python variables store values.

```python
nome = "Paolo"
eta = 50
prezzo = 19.90
attivo = True
```

The main types covered are `str`, `int`, `float`, and `bool`.

```python
x = 5
```

assigns a value, while:

```python
x == 5
```

checks equality.

## Key Takeaway

`=` assigns a value; `==` compares values.
""",

"02_python_fundamentals/02_lists_and_methods.md": """# 02 — Lists and Methods

Lists store multiple values in order.

```python
frutti = ["mela", "pera", "banana"]
```

Python uses zero-based indexing:

```python
frutti[0]
frutti[1]
```

Lists have methods such as:

```python
frutti.append("arancia")
frutti.remove("banana")
```

## Key Takeaway

A list is an ordered collection, and methods such as `.append()` and `.remove()` can modify it.
""",

"02_python_fundamentals/03_dictionaries_and_nested_data.md": """# 03 — Dictionaries and Nested Data

Dictionaries store values using keys.

```python
persona = {
    "nome": "Paolo",
    "eta": 50,
    "hobby": ["AI", "investimenti"]
}
```

Access:

```python
persona["nome"]
persona["hobby"][1]
```

API responses and JSON data often use nested structures.

## Key Takeaway

Dictionaries are useful for structured data because values can be accessed by meaningful keys.
""",

"02_python_fundamentals/04_loops_and_enumerate.md": """# 04 — Loops and enumerate()

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
""",

"02_python_fundamentals/05_functions_parameters_return.md": """# 05 — Functions, Parameters, and return

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
""",

"02_python_fundamentals/06_copy_and_mutation.md": """# 06 — Copying and Mutation

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
""",

"02_python_fundamentals/07_scope_and_errors.md": """# 07 — Scope and Common Errors

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
""",

"02_python_fundamentals/08_random_and_input_logic.md": """# 08 — Randomness and Input Logic

Python can generate random values with the `random` module.

```python
import random

numero = random.randint(1, 10)
```

`randint(1, 10)` returns an integer between 1 and 10, inclusive.

## Key Takeaway

Modules extend Python's capabilities. `import random` makes the module available to the program.
""",

"02_python_fundamentals/09_packages_pip_json_apis.md": """# 09 — Packages, pip, JSON, and APIs

External Python packages can add functionality.

```bash
pip install nome-pacchetto
```

JSON is a common format for exchanging structured data:

```json
{
  "nome": "Paolo",
  "eta": 50
}
```

A typical API flow is:

```text
Python program
      ↓
API request
      ↓
External service
      ↓
API response
      ↓
Python program
```

## Key Takeaway

Packages provide functionality; JSON structures data; APIs allow programs and services to communicate.
""",

"02_python_fundamentals/10_reading_ai_api_code.md": """# 10 — Reading AI API Code

A typical AI API workflow follows this pattern:

```python
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="MODEL",
    input="Explain what an API is in simple terms."
)

print(response.output_text)
```

## How to read it

`client = OpenAI()` creates a client object.

`client.responses.create(...)` calls a method and stores the returned response.

`response.output_text` accesses data exposed by the response object.

`print(response.output_text)` displays the generated text.

## Key Takeaway

The important pattern is:

```text
create/configure client
        ↓
call method
        ↓
receive response
        ↓
read response data
```

This pattern appears repeatedly in AI and API-based applications.
""",

"03_ai_api_basics/README.md": """# AI API Basics

This section connects Python fundamentals to AI/LLM applications.

## Core pattern

```text
Python
  ↓
Client
  ↓
API request
  ↓
LLM service
  ↓
Response object
  ↓
Generated text / structured data
```

The objective is to understand the architecture and code structure before moving into more advanced AI application development.
"""
}

for filename, content in FILES.items():
    path = Path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        print(f"SKIPPED: {path}")
    else:
        path.write_text(content, encoding="utf-8")
        print(f"CREATED: {path}")

print("Portfolio installation completed.")
