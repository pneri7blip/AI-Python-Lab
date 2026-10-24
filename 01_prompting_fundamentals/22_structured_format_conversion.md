# Structured Format Conversion

## Objective

Evaluate whether a language model can convert an unstructured customer support message into a structured JSON object while preserving relevant information and following an exact schema.

The exercise focuses on valid JSON, consistent field extraction, preservation of conditions and timing, and avoiding unsupported inferences.

---

## Initial Prompt

You are a data extraction specialist.

Convert the following customer support message into a JSON object.

Requirements:
- Use exactly these keys: "customer_name", "product", "issue", "purchase_date", "requested_action".
- Extract only information explicitly stated in the message.
- Use null for any field whose value is not provided.
- Preserve the meaning of the customer's issue and request.
- Do not infer missing details or add explanations.
- Return valid JSON only, with no Markdown code fences or additional text.

Customer message:

"Hello, I'm Maria Rossi. I bought a NovaSound X2 headset on March 14, 2026. Since yesterday, the left earcup has stopped producing sound, although the right side still works. I'd like a replacement if the product is covered by the warranty."

---

## Initial Outputs

### GPT

> {
>   "customer_name": "Maria Rossi",
>   "product": "NovaSound X2 headset",
>   "issue": "Since yesterday, the left earcup has stopped producing sound, although the right side still works.",
>   "purchase_date": "March 14, 2026",
>   "requested_action": "A replacement if the product is covered by the warranty."
> }

### Gemini

> {
>   "customer_name": "Maria Rossi",
>   "product": "NovaSound X2 headset",
>   "issue": "the left earcup has stopped producing sound, although the right side still works",
>   "purchase_date": "March 14, 2026",
>   "requested_action": "I'd like a replacement if the product is covered by the warranty"
> }

---

## Initial Evaluation

Both models returned the five requested keys and preserved the main information in the source message.

- **Customer and product:** Both extracted the name and product correctly.
- **Issue:** GPT preserved the relative timing, "Since yesterday," as well as the distinction between the left and right earcups. Gemini preserved the two earcup details but omitted the timing.
- **Purchase date:** Both preserved the date as stated.
- **Requested action:** Both retained the condition that a replacement is requested only if the product is covered by the warranty.
- **Output format:** Both outputs appeared to be valid JSON, with no additional explanatory text.

The initial test revealed a small difference in extraction completeness. It did not test missing values, because all five fields had information available in the source.

---

## Prompt Revision 1

The revised prompt made the schema and information-preservation requirements more explicit.

You are a data extraction specialist.

Convert the customer support message into a JSON object that follows the exact schema below.

Required schema:
{
  "customer_name": "string or null",
  "product": "string or null",
  "issue": "string or null",
  "purchase_date": "string or null",
  "requested_action": "string or null"
}

Requirements:
- Include exactly the five keys shown above. Do not add or omit keys.
- Extract all relevant information explicitly stated for each field, including relevant timing and conditions.
- Use null (without quotation marks) only when the source does not provide the information for that field.
- Preserve conditions, uncertainty, and distinctions stated in the original message.
- Use concise, self-contained field values rather than copying unnecessary conversational wording.
- Do not infer missing facts, such as warranty eligibility.
- Return valid JSON only. Do not include Markdown fences, comments, or explanations.

Customer message:

"Hello, I'm Maria Rossi. I bought a NovaSound X2 headset on March 14, 2026. Since yesterday, the left earcup has stopped producing sound, although the right side still works. I'd like a replacement if the product is covered by the warranty."

---

## Revised Outputs

### GPT

> {
>   "customer_name": "Maria Rossi",
>   "product": "NovaSound X2 headset",
>   "issue": "Since yesterday, the left earcup has stopped producing sound, although the right side still works.",
>   "purchase_date": "March 14, 2026",
>   "requested_action": "Replacement if the product is covered by the warranty."
> }

### Gemini

> {
>   "customer_name": "Maria Rossi",
>   "product": "NovaSound X2 headset",
>   "issue": "Since yesterday, the left earcup has stopped producing sound, although the right side still works",
>   "purchase_date": "March 14, 2026",
>   "requested_action": "Replacement if the product is covered by the warranty"
> }

---

## Evaluation

| Criterion | GPT | Gemini |
|---|---|---|
| Required keys present | Yes | Yes |
| No extra keys | Yes | Yes |
| Relevant issue timing preserved | Yes | Yes |
| Left/right distinction preserved | Yes | Yes |
| Warranty condition preserved | Yes | Yes |
| No unsupported warranty claim | Yes | Yes |
| JSON-only output | Yes | Yes |

The revised prompt addressed the omission observed in Gemini's initial issue field: both models now included "Since yesterday."

The `requested_action` field was also normalized into a concise phrase by both models, while retaining the warranty condition. Neither model claimed that the product was actually covered by the warranty.

The only visible differences were minor stylistic choices, such as punctuation and capitalization. These do not materially change the extracted information.

The revision improved the observed completeness of the output for this example, but the test involved only one message and two models. It does not establish general reliability or prove that the revised prompt will always perform better.

---

## Key Takeaway

Structured extraction requires more than producing syntactically valid JSON. A useful result must also follow the required schema, preserve relevant details, retain conditions and uncertainty, and avoid inventing missing information.

Explicit schemas and extraction rules can help make outputs more consistent. In production workflows, JSON syntax should also be validated automatically, and required fields and value types should be checked separately. A syntactically valid JSON object can still contain incomplete or incorrect information.

Further testing with missing fields, ambiguous dates, conflicting details, and conditional requests would be needed to evaluate robustness beyond this example.
