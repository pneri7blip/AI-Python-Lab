# Conversation-to-Structured-Data Extraction

## Objective

Evaluate how accurately an AI model can transform conversational information into structured data.

The exercise focuses on:

- Extracting specific fields from a conversation.
- Preserving the meaning of the original information.
- Handling missing information without inventing values.
- Recognizing explicit corrections.
- Distinguishing confirmed information from uncertain information.
- Producing valid, consistently structured JSON.

The scenario simulates extracting information from employee conversations in an IT support environment.

---

## Test 1: Basic Information Extraction

### Initial Prompt

You are an AI assistant responsible for extracting structured information from IT support conversations.

Analyze the conversation below and convert the information into a valid JSON object.

Conversation:

Employee: "My company laptop keeps disconnecting from the office Wi-Fi."  
Assistant: "Which department do you work in?"  
Employee: "Finance."  
Assistant: "How urgent is the issue?"  
Employee: "High priority. I have a financial report to submit this afternoon."  
Assistant: "What is your name?"  
Employee: "Alex."

Extract the following fields:

- `employee_name`
- `department`
- `issue_description`
- `priority`
- `priority_reason`
- `device_identifier`
- `contact_email`

Instructions:

- Extract only information explicitly provided in the conversation.
- Do not infer or invent missing values.
- If a field is not available, use `null`.
- Preserve the original meaning of the information.
- Return only valid JSON.
- Do not include explanations or Markdown formatting.

### GPT Output

> ```json
> {
>   "employee_name": "Alex",
>   "department": "Finance",
>   "issue_description": "Company laptop keeps disconnecting from the office Wi-Fi.",
>   "priority": "High",
>   "priority_reason": "A financial report needs to be submitted this afternoon.",
>   "device_identifier": null,
>   "contact_email": null
> }
> ```

### Gemini Output

> ```json
> {
>   "employee_name": "Alex",
>   "department": "Finance",
>   "issue_description": "My company laptop keeps disconnecting from the office Wi-Fi.",
>   "priority": "High",
>   "priority_reason": "I have a financial report to submit this afternoon.",
>   "device_identifier": null,
>   "contact_email": null
> }
> ```

### Test 1 Evaluation

| Criterion | GPT | Gemini |
|---|---|---|
| Correct employee name | Yes | Yes |
| Correct department | Yes | Yes |
| Correct issue description | Yes | Yes |
| Correct priority | Yes | Yes |
| Preserves priority reason | Yes | Yes |
| Handles missing fields | Yes | Yes |
| Produces valid JSON | Yes | Yes |

**Observation:** Both models successfully extract all available information and use `null` for fields that are not present in the conversation. There is a minor difference in wording: GPT uses a more concise, impersonal description of the priority reason, while Gemini preserves the employee's first-person wording. Both preserve the original meaning.

---

## Test 2: Handling Corrections and Uncertain Information

The second test introduces two additional challenges:
1. The employee explicitly corrects previously provided information.
2. The employee provides a device identifier but expresses uncertainty about its accuracy.

The objective is to determine whether the model can distinguish the latest confirmed information from outdated or uncertain details.

### Revised Prompt

You are an AI assistant responsible for extracting structured information from IT support conversations.

Analyze the conversation below and convert the information into a valid JSON object.

Conversation:

Employee: "My laptop keeps disconnecting from the office Wi-Fi."  
Assistant: "Which department do you work in?"  
Employee: "Marketing."  
Employee: "Sorry, I meant Finance. I recently transferred departments."  
Assistant: "How urgent is the issue?"  
Employee: "Initially I thought it was medium priority, but actually it's high priority. I need to submit a financial report this afternoon."  
Assistant: "Do you know your laptop's device identifier?"  
Employee: "I think it might be LT-2048, but I'm not completely sure."

Extract the following fields:

- `department`
- `issue_description`
- `priority`
- `priority_reason`
- `device_identifier`
- `contact_email`

Instructions:

- Use the latest explicit correction when the employee changes previously provided information.
- Distinguish confirmed information from uncertain information.
- Do not treat uncertain information as confirmed.
- If a field is missing or cannot be reliably confirmed, use `null`.
- Do not infer or invent missing values.
- Preserve the original meaning of the conversation.
- Return only valid JSON.
- Do not include explanations or Markdown formatting.

### GPT Output

> ```json
> {
>   "department": "Finance",
>   "issue_description": "Laptop keeps disconnecting from the office Wi-Fi.",
>   "priority": "High",
>   "priority_reason": "Needs to submit a financial report this afternoon.",
>   "device_identifier": null,
>   "contact_email": null
> }
> ```

### Gemini Output

> ```json
> {
>   "department": "Finance",
>   "issue_description": "My laptop keeps disconnecting from the office Wi-Fi.",
>   "priority": "High",
>   "priority_reason": "I need to submit a financial report this afternoon.",
>   "device_identifier": null,
>   "contact_email": null
> }
> ```

### Test 2 Evaluation

| Criterion | GPT | Gemini |
|---|---|---|
| Applies department correction | Yes | Yes |
| Uses the latest priority | Yes | Yes |
| Preserves priority reason | Yes | Yes |
| Rejects uncertain device identifier | Yes | Yes |
| Handles missing contact email | Yes | Yes |
| Produces valid JSON | Yes | Yes |

**Observation:** Both models correctly replace the original department with Finance and retain High as the final priority. They also reject the uncertain device identifier rather than treating "LT-2048" as confirmed. This is particularly important in business workflows, where an incorrectly extracted identifier could cause a support request to be associated with the wrong device.

---

## Cross-Test Analysis

| Capability | Test 1 | Test 2 |
|---|---|---|
| Basic information extraction | Successful | Successful |
| Missing-field handling | Successful | Successful |
| Meaning preservation | Successful | Successful |
| Correction handling | Not tested | Successful |
| Uncertainty handling | Not tested | Successful |
| JSON generation | Successful | Successful |

---

## Key Findings

1. **Structured extraction requires more than identifying keywords:** The model must understand which conversational details correspond to each requested field and preserve their meaning.
2. **Missing information should remain missing:** Using `null` prevents the model from filling gaps with invented information. This is particularly useful when extracted data will be passed to another system.
3. **Corrections must take precedence over outdated information:** The second test demonstrates that both models can recognize an explicit correction and use the latest confirmed value.
4. **Uncertainty must not become false certainty:** The device identifier is mentioned, but the employee is unsure about it. Both models correctly return `null`. This distinction matters because structured data can appear authoritative even when its original source was uncertain.
5. **Similar outputs do not establish identical reliability:** Both models performed well in these scenarios. However, two successful tests are not sufficient to establish consistent performance across different conversations or more complex data extraction tasks.

---

## Limitations

- Only two conversational scenarios were tested.
- No automated JSON schema validation was performed.
- The exercise does not test conflicting information that remains unresolved.
- It does not distinguish between missing, uncertain, and explicitly rejected values in the output schema: all are represented as `null`.
- Repeated runs and more diverse scenarios would be needed to assess consistency.

A production system would benefit from a more expressive data structure that records both the extracted value and its confidence or verification status. For example, an uncertain device identifier could be represented separately from a field that was never provided.

---

## Conclusion

This exercise demonstrates how AI models can transform conversational information into structured data while preserving meaning, handling missing fields, applying corrections, and avoiding unsupported assumptions.

The two tests show that both GPT and Gemini successfully handled the scenarios presented.

The most important lesson is that structured extraction must preserve not only the information itself, but also its reliability.

**Core takeaway:** Reliable conversation-to-data extraction requires the model to distinguish between what was explicitly stated, what was corrected, what remains uncertain, and what was never provided.
