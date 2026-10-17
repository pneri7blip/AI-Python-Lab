# Entity Extraction & Multi-Task Inference

## Objective

Evaluate how prompt instructions affect structured information extraction and multi-task classification.

The exercise asks two language models to determine sentiment, detect anger, extract product and brand names, and identify unresolved customer issues in a single JSON response.

---

## Initial Prompt

You are assisting a customer operations analyst.

Analyze the following customer message and return a valid JSON object with exactly these fields:

- "Sentiment": "positive", "negative", or "neutral"
- "Anger": a boolean value (true or false)
- "Product": the name of the product mentioned, or null if no product is identified
- "Brand": the brand name, or null if no brand is identified
- "Issue": a concise description of the main problem, or null if no problem is reported

Apply these rules:
- Determine sentiment from the message as a whole.
- Set "Anger" to true only when the message explicitly expresses anger or strong irritation. A complaint alone does not automatically mean anger.
- Extract product and brand names only when explicitly supported by the message. Do not guess missing information.
- Keep the issue concise and faithful to the message.
- Do not add fields or explanations.
- Return valid JSON only.

Customer Message:

"I bought the AeroBrew Mini from Novatek three weeks ago. It makes excellent coffee, but yesterday it stopped heating the water. I've unplugged it and tried again twice, with no success. I'm really frustrated because I need it every morning, and support still hasn't replied to my message from Monday."

---

## Initial Outputs

### GPT-5.6 Luna

> {
>   "Sentiment": "negative",
>   "Anger": true,
>   "Product": "AeroBrew Mini",
>   "Brand": "Novatek",
>   "Issue": "The coffee maker stopped heating water, and customer support has not replied to the message sent on Monday."
> }

### Gemini 3.1 Pro

> {
>   "Sentiment": "negative",
>   "Anger": true,
>   "Product": "AeroBrew Mini",
>   "Brand": "Novatek",
>   "Issue": "Stopped heating the water and customer support has not replied"
> }

---

## Issue Identified

Both models agreed on all five fields, including the negative sentiment, product name, brand name, and two unresolved issues.

However, both classified anger as "true" based on the customer's statement, "I'm really frustrated."

Frustration can indicate dissatisfaction without necessarily establishing explicit anger. The initial prompt did not sufficiently distinguish these related emotional states.

The issue descriptions also differed slightly in detail, although both captured the equipment failure and the unanswered support request.

---

## Prompt Revision 1

The revised prompt clarified the anger classification criteria and required the issue field to capture separate unresolved problems.

You are assisting a customer operations analyst.

Analyze the following customer message and return a valid JSON object with exactly these fields:

- "Sentiment": "positive", "negative", or "neutral"
- "Anger": a boolean value (true or false)
- "Product": the name of the product mentioned, or null if no product is identified
- "Brand": the brand name, or null if no brand is identified
- "Issue": a concise description of the main problem, or null if no problem is reported

Apply these rules:
- Determine sentiment from the message as a whole.
- Set "Anger" to true only when the text explicitly indicates anger, rage, or strong irritation directed at a person, company, or situation.
- Do not classify disappointment, worry, inconvenience, or frustration alone as anger unless the wording also clearly indicates anger or strong irritation.
- A complaint or a negative sentiment does not automatically mean anger.
- Extract product and brand names only when explicitly supported by the message. Do not guess missing information.
- Include the main product or service problem and any separate unresolved customer-support problem in "Issue", if both are reported.
- Keep "Issue" concise and faithful to the message.
- Use null for "Product", "Brand", or "Issue" only when the corresponding information is not identified or reported.
- Do not add fields or explanations.
- Return valid JSON only.

Customer Message:

"I bought the AeroBrew Mini from Novatek three weeks ago. It makes excellent coffee, but yesterday it stopped heating the water. I've unplugged it and tried again twice, with no success. I'm really frustrated because I need it every morning, and support still hasn't replied to my message from Monday."

---

## Revised Outputs

### GPT-5.6 Luna

> {
>   "Sentiment": "negative",
>   "Anger": false,
>   "Product": "AeroBrew Mini",
>   "Brand": "Novatek",
>   "Issue": "The coffee maker stopped heating water despite two restart attempts, and customer support has not replied to the message sent on Monday."
> }

### Gemini 3.1 Pro

> {
>   "Sentiment": "negative",
>   "Anger": false,
>   "Product": "AeroBrew Mini",
>   "Brand": "Novatek",
>   "Issue": "The machine stopped heating water and customer support has not replied to a message sent on Monday."
> }

---

## Evaluation

The revised prompt produced agreement between both models on all five fields.

The most important change was the anger classification, which changed from "true" to "false" in both outputs. This was consistent with the revised instruction not to treat frustration alone as evidence of anger.

Both models retained the correct product and brand names and identified the equipment failure and unanswered support request. Their issue descriptions differed slightly in detail but preserved the same essential information.

The comparison demonstrates that explicit decision rules can change model classifications and improve consistency. However, agreement between two models does not independently prove that a classification is correct; the criteria must still be evaluated against the intended annotation standard.

---

## Key Takeaway

Multi-task prompting combines several related classification and extraction tasks in a single request. Clear field definitions, explicit decision boundaries, and a fixed output schema help make the results more consistent and usable.

For professional evaluation work, it is important to assess each field separately, distinguish related but different concepts, and verify that the output follows the required schema.
