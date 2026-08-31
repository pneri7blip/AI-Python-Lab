# Condition Checking in Prompt Engineering

## Objective

Explore how a prompt can ask an AI model to check whether a piece of text satisfies a specific condition before producing an answer.

## Example Prompt

Determine whether the following customer review contains a complaint about delivery.

Return only `YES` or `NO`.

```text
The headphones sound excellent, but they arrived three days later than expected.
```

## Expected Output

```text
YES
```

## What I Learned

A prompt can ask the model to check a specific condition before generating its answer. Explicitly defining the condition and the expected output makes the model's response more consistent and easier to evaluate.