# Context-Aware Conversation Management

## Objective

Evaluate how well an AI assistant manages a multi-turn conversation while collecting information required to complete a business process.

The exercise focuses on:

- Retaining information across multiple conversation turns.
- Identifying missing information.
- Avoiding unnecessary or repeated questions.
- Tracking whether required conditions have been satisfied.
- Moving to the next stage only when the necessary information is available.
- Requesting user confirmation before proceeding.

The scenario simulates an IT support request workflow.

---

## Scenario

An employee contacts an AI assistant because their company laptop repeatedly disconnects from the office Wi-Fi.

The assistant needs to collect four required fields:

1. Employee name
2. Department
3. Technical issue
4. Priority level

The request must not be considered complete until all four fields are available. Once collected, the assistant must present a summary and request confirmation.

---

## Test 1: Identifying Missing Information

### Initial Prompt

You are an AI assistant helping users submit IT support requests for a company.

Your task is to guide the user through the request process over multiple conversation turns.

Conversation so far:

Customer: "My company laptop keeps disconnecting from the office Wi-Fi."  
Assistant: "I can help you prepare an IT support request. Which department do you work in?"  
User: "Finance."  
Assistant: "How urgent is the issue?"  
User: "High priority. I have a financial report to submit this afternoon."

The user's latest message is:  
"Okay, please submit the request."

Respond naturally to the latest message using the conversation history.

Instructions:
- Retain the information already provided: the laptop's recurring Wi-Fi disconnections, the Finance department, and the high priority caused by a report due this afternoon.
- Identify what information, if any, is still needed before the request can be submitted.
- Ask only for the next necessary piece of information, if one is missing.
- Do not ask the user to repeat information already provided.
- Do not invent missing details, such as the user's name, device identifier, or contact information.
- Do not claim that a support request has been submitted or that an IT ticket has been created.
- Do not assume that you have access to the company's IT systems.
- Keep the response concise, professional, and helpful.
- Output only the reply to the user.

### GPT Output

> «I have the details so far:
> 
> - Issue: Company laptop repeatedly disconnects from the office Wi-Fi.
> - Department: Finance.
> - Priority: High, because you have a financial report due this afternoon.
> 
> Before proceeding, what is your name so the IT support request can be correctly identified?»

### Gemini Output

> «Before I can finalize the request, could you please provide your name and contact email?»

### Initial Evaluation

| Criterion | GPT | Gemini |
|---|---|---|
| Retains the technical issue | Yes | Not explicitly repeated |
| Retains the department | Yes | Not explicitly repeated |
| Retains the priority and its reason | Yes | Not explicitly repeated |
| Identifies missing information | Yes | Yes |
| Requests only one missing field | Yes | No |
| Avoids claiming submission | Yes | Yes |

**Observation:** Both models recognize that additional information is needed before proceeding. GPT summarizes the information already collected and asks for the employee's name only. Gemini asks for both the name and contact email. However, the original prompt does not define a required-field list, so it is impossible to determine whether requesting an email is genuinely unnecessary or simply an assumption about the company's workflow.

This exposes an important limitation in the initial test: the assistant has not been given an explicit definition of what constitutes a complete request.

---

## Test 2: Tracking Required Fields and Process Completion

The second test introduces explicit requirements and a later conversation turn. The objective is to determine whether the models can recognize when all mandatory information has been collected and move from information gathering to request review.

### Revised Prompt

You are an AI assistant helping employees submit IT support requests.

Your task is to collect the required information through a multi-turn conversation and prepare a complete support request.

A request can only be prepared when all four required fields are available:

1. Employee name
2. Department
3. Description of the technical issue
4. Priority level

Conversation so far:

User: "My company laptop keeps disconnecting from the office Wi-Fi."  
Assistant: "Which department do you work in?"  
User: "Finance."  
Assistant: "How urgent is the issue?"  
User: "High priority. I have a financial report to submit this afternoon."  
Assistant: "What is your name?"  
User: "Alex."

The user's latest message is:  
"Great, let's proceed."

Instructions:
- Use all information already provided in the conversation.
- Identify whether all four required fields are available.
- If a required field is missing, ask only for the next missing field.
- If all four fields are available, present a structured summary of the request for the user's confirmation.
- Do not ask for information that is not required.
- Do not invent information.
- Do not claim that a request has been submitted or that an IT ticket has been created.
- Keep the response concise and professional.
- Output only the reply to the user.

### GPT Output

> «All required information has been collected. Please review the support request below and confirm that the details are correct.
> 
> **IT Support Request**
> - **Employee name:** Alex
> - **Department:** Finance
> - **Technical issue:** Company laptop keeps disconnecting from the office Wi-Fi.
> - **Priority:** High
> - **Reason for priority:** A financial report must be submitted this afternoon.
> 
> Would you like to confirm this support request?»

### Gemini Output

> «Here is the summary of your support request:
> 
> - **Name:** Alex
> - **Department:** Finance
> - **Issue Description:** Company laptop keeps disconnecting from office Wi-Fi
> - **Priority Level:** High (Financial report due this afternoon)
> 
> Please confirm if these details are correct so we can proceed with your request.»

### Second Evaluation

| Criterion | GPT | Gemini |
|---|---|---|
| Recovers all four required fields | Yes | Yes |
| Retains the relevant conversation context | Yes | Yes |
| Recognizes that no required field is missing | Yes | Yes |
| Presents a structured summary | Yes | Yes |
| Requests confirmation | Yes | Yes |
| Avoids claiming that a ticket was submitted | Yes | Yes |

**Observation:** Both models successfully recognize that all four required fields are available. They move to the next stage rather than asking additional questions. Both present the collected information and request confirmation before proceeding. GPT separates the priority from its justification, while Gemini combines them into one field. Both approaches preserve the relevant information.

---

## Cross-Test Analysis

| Capability | Test 1 | Test 2 |
|---|---|---|
| Context retention | Retains information collected so far | Recovers information across additional turns |
| Missing-information detection | Identifies that the employee name is missing | Recognizes that no required field is missing |
| Information collection | Requests missing information | No additional collection required |
| Process management | Does not prematurely submit the request | Moves to the review stage |
| User confirmation | Not yet applicable | Requests confirmation before proceeding |

---

## Key Findings

1. **Context retention must support decision-making:** Remembering conversation details is only part of the task. The assistant must use those details to determine what should happen next.
2. **Missing-information detection requires explicit requirements:** The first test demonstrates that models may make different assumptions about what information is necessary. Defining mandatory fields makes the expected behavior more predictable and easier to evaluate.
3. **Multi-turn workflows require state tracking:** The second test demonstrates a different capability: recognizing that the information-gathering stage is complete and moving to the next stage. The assistant must not continue asking questions once all required fields are available.
4. **Completion and confirmation are separate stages:** Having all the necessary information does not mean the request has been submitted. The assistant must present the information for review and obtain confirmation before any subsequent action.
5. **Similar outputs do not prove identical reliability:** Both models produced suitable responses in the second test. However, these results represent only one scenario and do not establish consistent performance across different conversations.

---

## Limitations

- Only one IT support scenario was tested.
- The exercise does not test actual ticket creation or integration with an IT service management platform.
- The required fields were explicitly defined in the second test, making the completion criteria easier to follow.
- The exercise does not test conflicting information, corrections to previously supplied details, or users changing their decisions.
- Repeated runs would be necessary to evaluate consistency.

---

## Conclusion

This exercise demonstrates how an AI assistant can manage a multi-turn business workflow by retaining context, identifying missing information, tracking required fields, and advancing through defined process stages.

The initial test reveals that models can make different assumptions about missing information. The second test reduces this ambiguity by explicitly defining the required fields and the conditions for moving forward.

**Core takeaway:** A reliable conversational assistant must do more than remember previous messages. It must understand the current state of the process, determine what is still needed, and advance only when the appropriate conditions have been met.
