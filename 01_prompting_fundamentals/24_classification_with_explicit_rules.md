# Classification with Explicit Rules

## Objective

Evaluate whether an LLM can classify customer support messages into predefined categories using explicit rules, especially when a message contains multiple issues with different levels of importance.

---

## Initial Prompt

You are a support-ticket classification assistant. Assign exactly one category to the customer message using the rules below.

Categories:

- BILLING: payments, invoices, refunds, or unexpected charges.
- TECHNICAL: software errors, malfunctioning features, or technical failures.
- ACCOUNT: login problems, password resets, or account access.
- OTHER: requests that do not fit the categories above.

Rules:

- Choose the category that best matches the customer's main problem, not merely a secondary detail.
- If multiple issues are mentioned, classify according to the issue that most directly prevents the customer from completing their primary task.
- Do not infer facts that are not stated.
- Output only the category label, with no explanation.

---

## Test Cases and Initial Outputs

### Test 1: Technical Error with a Billing Deadline

**Customer message:**

"I can log in without any problems, but when I try to download my invoice, the page displays an error and nothing happens. I need the invoice today because my company has to process the payment before the end of the day."

> **GPT:** TECHNICAL  
> **Gemini:** TECHNICAL

**Evaluation:**

Both models classified the message as "TECHNICAL". The immediate obstacle is a page error preventing the customer from downloading the invoice. The payment deadline provides urgency but does not change the nature of the reported malfunction.

---

### Test 2: Duplicate Charge with an Account Access Problem

**Customer message:**

"I was charged twice for my subscription this month. I contacted support last week, but now I can't log in to check whether the refund has been processed. I need the money back as soon as possible."

> **GPT:** BILLING  
> **Gemini:** BILLING

**Evaluation:**

Both models selected "BILLING". The duplicate charge and the request for a refund are the main concerns, while the login problem is presented as an obstacle to checking the refund status.

---

### Test 3: Account Access Problem with a Financial Consequence

**Customer message:**

"I can't log in to my account, and I need to access my invoices before today's payment deadline. If I miss the deadline, I may incur a late fee. I've tried resetting my password twice, but I still can't get in."

> **GPT:** ACCOUNT  
> **Gemini:** ACCOUNT

**Evaluation:**

Both models selected "ACCOUNT". The immediate problem is the inability to log in, despite two password reset attempts. The potential late fee is a consequence of the access problem rather than evidence of an existing billing error.

---

## Results Summary

| Test | Expected Category | GPT | Gemini |
|---|---|---|---|
| Technical error blocks invoice download | TECHNICAL | TECHNICAL | TECHNICAL |
| Duplicate charge and login problem | BILLING | BILLING | BILLING |
| Login problem creates risk of a late fee | ACCOUNT | ACCOUNT | ACCOUNT |

Both models agreed on all three test cases and returned only the requested category labels.

This represents 3/3 model agreements across the tested cases, not a statistically meaningful accuracy estimate. The expected categories were determined by interpreting the prompt rules and the primary problem in each message.

---

## Limitations and Next Steps

The tests revealed a potential limitation in the classification rules: the instruction to prioritize the issue that prevents the customer's primary task can leave room for interpretation when a message combines an immediate technical or account problem with a financial consequence.

For a production workflow, the classification policy should define how to handle these situations consistently. For example, it could specify whether to prioritize the immediate operational obstacle, the underlying customer request, or a defined business priority.

Further evaluation should include more examples, borderline cases, and a reference set of human-assigned labels. Classification performance should be measured against those labels rather than relying only on agreement between two models.

---

## Key Takeaway

Explicit classification rules help constrain model outputs, but they do not eliminate ambiguity when several issues appear in the same message.

A reliable classification workflow requires clear category definitions, consistent priority rules, and evaluation against representative labeled examples. Agreement between models is useful evidence to inspect, but it does not independently establish correctness.
