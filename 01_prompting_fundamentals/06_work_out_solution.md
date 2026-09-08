# Exercise 6: Instruct the Model to Work Out Its Own Solution

## Objective
Give the model time to independently calculate the correct result before evaluating a user-submitted answer. This helps prevent the model from prematurely accepting incorrect calculations or conclusions.

## Prompt Used
> Your task is to determine if the vendor's cost calculation is correct or not.
>
> To solve the problem, do the following:
> 1. First, work out your own solution to the problem step-by-step.
> 2. Compare your solution to the vendor's solution and evaluate if the vendor's total is correct or not.
> 3. Do not decide if the vendor's solution is correct until you have done the problem yourself.
>
> Use the following format:
>
> Project Estimate:
> ```
> <project estimate text>
> ```
>
> Vendor Solution:
> ```
> <vendor solution text>
> ```
>
> Actual Solution:
> ```
> <steps to work out the solution and your actual calculation>
> ```
>
> Is the vendor's solution the same as actual solution just calculated:
> ```
> yes or no
> ```
>
> Vendor Grade:
> ```
> correct or incorrect
> ```
>
> Project Estimate: ```<project_text>```
> Vendor Solution: ```<vendor_text>```

## Input Text
```text
Project Estimate:
Cloud Infrastructure Setup:
- Architecture Planning: 20 hours at $150/hr
- Database Migration: 15 hours at $120/hr
- Support Retainer: Flat fee of $100, plus $10/hr for 10 hours

Vendor Solution:
1. Architecture Planning: 20 * $150 = $3,000
2. Database Migration: 15 * $120 = $1,800
3. Support Retainer: $100 + ($100 * 10) = $1,100
Total Cost: $3,000 + $1,800 + $1,100 = $5,900
```

## Model Output
```text
Actual Solution:
1. Architecture Planning: 20 hours * $150/hr = $3,000
2. Database Migration: 15 hours * $120/hr = $1,800
3. Support Retainer: $100 flat fee + (10 hours * $10/hr) = $100 + $100 = $200
Total Cost: $3,000 + $1,800 + $200 = $5,000

Is the vendor's solution the same as actual solution just calculated:
No

Vendor Grade:
Incorrect
```

## Evaluation

Tested with two LLMs, **ChatGPT** and **Gemini 3.1 Pro**, to evaluate prompt portability and consistency. Both models independently calculated the expected total before comparing it with the vendor's solution and correctly identified the vendor's calculation error.

## Key Takeaway

Requiring the model to independently calculate the expected result before comparing it with a user-provided answer can reduce the risk of accepting incorrect conclusions. Explicitly separating calculation from evaluation makes the verification process more reliable.
