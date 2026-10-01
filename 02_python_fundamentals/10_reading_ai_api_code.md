# 10 — Reading AI API Code

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
