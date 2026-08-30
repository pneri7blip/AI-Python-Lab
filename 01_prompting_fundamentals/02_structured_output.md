# Structured Output in Prompt Engineering

## Objective

Explore how explicit output formatting instructions can make AI responses easier to process and reuse.

## Example Prompt

Extract the following information from the product description and return the result as JSON:

- product_name
- price
- currency
- availability

Product description:

```text
The new Aurora Wireless Headphones are available for €129.99 and are currently in stock.
```

## Expected Output

```json
{
  "product_name": "Aurora Wireless Headphones",
    "price": 129.99,
      "currency": "EUR",
        "availability": "in stock"
        }
        ```

        ## What I Learned

        Requesting a structured format such as JSON makes AI output more predictable and easier for applications to process programmatically.