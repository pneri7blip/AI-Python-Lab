# Multi-Turn Conversation and Context Retention

## Objective

Evaluate how well an AI chatbot uses conversation history to answer a customer's latest message.

The exercise focuses on three practical capabilities:

- **Context retention:** preserving relevant details across multiple turns.
- **Instruction adherence:** following explicit operational and communication constraints.
- **Reliable customer support:** suggesting useful next steps without inventing actions, access, or commitments.

The goal is to improve chatbot behavior through prompt iteration and evidence-based evaluation, rather than assuming that a more detailed prompt will automatically produce a perfect response.

---

## Scenario

A customer contacts an online electronics store because an order has not arrived as expected.

The conversation history contains three important facts:

- **Order number:** "#4821"
- **Expected delivery:** Monday
- **Delivery option:** Express, with an additional €12 charge

The customer's latest message is:

> «Can you tell me what happens next?»

The chatbot should use the existing context to explain a reasonable next step without pretending to access order systems or promising an outcome.

---

## Test 1: Initial Prompt

### Prompt

You are a customer support chatbot for an online electronics store.

Your task is to help customers resolve delivery issues through a conversation.

Conversation so far:

Customer: "My order #4821 was supposed to arrive on Monday, but it hasn't arrived."  
Assistant: "I'm sorry about the delay. Could you tell me which delivery option you selected?"  
Customer: "Express delivery. I paid an extra €12 for it."

The customer's latest message is:  
"Can you tell me what happens next?"

Respond naturally to the customer's latest message. Use the information from the conversation, acknowledge the issue, and explain a reasonable next step.

Do not invent the order's current status, claim to have accessed the order system, promise a refund, or guarantee a delivery date. Do not ask the customer to repeat information already provided.

### GPT Output

> «I’m sorry your order #4821 hasn’t arrived as expected, especially since you paid an extra €12 for express delivery.
> 
> The next step is to check the delivery status and investigate the delay. Our support team should verify what happened to your shipment and review the express delivery service you paid for.
> 
> Once the situation has been checked, we can explain the available options, including whether you may be eligible for compensation for the delayed express service.
> 
> I can’t confirm the current status or promise a delivery date just yet, but we should help you get a clear update on what happens next.»

### Gemini Output

> «I completely understand your frustration, especially since you paid extra for express delivery to have your order arrive on Monday.
> 
> Next, I will look into order #4821 with our shipping carrier to trace the current location of your package and find out what caused the delay. Once I check the tracking details, I'll update you on the progress so we can get this resolved for you.
> 
> Could you please confirm the email address associated with your account so I can verify your order details?»

---

## Initial Evaluation

| Criterion | GPT | Gemini |
|---|---|---|
| Retains relevant context | Yes | Yes |
| Suggests a practical next step | Yes | Yes |
| Claims to perform an action | No | Yes |
| Implies access to operational systems | No | Yes |
| Requests unnecessary information | No | Yes, an email address |
| Avoids unsupported commitments | Mostly | No, promises an update |

**Observation:** Both models understand the customer's situation, but their operational behavior differs. GPT proposes a reasonable process without claiming to execute it. Gemini says it will investigate the shipment and provide an update, implying capabilities that the prompt has not established. It also requests additional personal information without explaining why it is necessary.

GPT introduces a possible compensation outcome. Although it does not guarantee compensation, this is an area where more explicit constraints could improve control.

---

## Test 2: Revised Prompt

The second prompt makes the expected behavior more explicit. Instead of relying on a general instruction to respond naturally, it specifies which details to retain, what the next step should cover, and which claims or requests to avoid.

### Revised Prompt

You are a customer support chatbot for an online electronics store.

Your task is to respond to the customer's latest message using the conversation history.

Conversation so far:

Customer: "My order #4821 was supposed to arrive on Monday, but it hasn't arrived."  
Assistant: "I'm sorry about the delay. Could you tell me which delivery option you selected?"  
Customer: "Express delivery. I paid an extra €12 for it."

Customer's latest message:  
"Can you tell me what happens next?"

Instructions:
- Retain and use the relevant details already provided: order #4821, the missed Monday delivery, express delivery, and the extra €12 charge.
- Acknowledge the customer's concern and explain one practical next step.
- Explain what the support team should verify, without claiming that you have performed or initiated any action.
- Do not claim access to order systems, tracking information, or the shipping carrier.
- Do not promise a follow-up, delivery date, refund, or compensation.
- Do not ask for information that is not necessary to explain the next step.
- Do not ask the customer to repeat information already provided.
- Use a concise, empathetic, professional tone.
- Output only the reply to the customer.

### GPT Output

> «I’m sorry that your order #4821 hasn’t arrived as expected, especially since you paid an extra €12 for express delivery.
> 
> The next step is to contact our support team and ask them to review your order. They should verify the shipment status, investigate why the Monday delivery was missed, and check the express delivery terms to determine whether the €12 charge is eligible for a refund.
> 
> I understand how frustrating this is, and the review will help clarify what options are available to resolve the delay.»

### Gemini Output

> «I understand your frustration with order #4821 missing its Monday delivery, especially after paying an extra €12 for Express delivery.
> 
> The next step is to check the shipment status. The support team needs to verify the latest tracking updates with the carrier to see where your package is located and determine why it was delayed.»

---

## Revised Evaluation

| Criterion | GPT | Gemini |
|---|---|---|
| Retains the order number and delivery context | Yes | Yes |
| Acknowledges the customer's concern | Yes | Yes |
| Explains a practical next step | Yes | Yes |
| Claims to have performed an action | No | No |
| Requests unnecessary information | No | No |
| Avoids promising a refund or compensation | Mostly | Yes |
| Follows the requested concise style | Mostly | Yes |

### What Changed?

- **GPT:** The revised response no longer suggests that compensation may be available in general terms. However, it explicitly mentions checking whether the €12 charge is eligible for a refund. This is not a refund promise, but it introduces a specific potential remedy despite the instruction not to promise refunds or compensation. The wording is therefore useful but not perfectly aligned with the intended constraint.
- **Gemini:** The revised response removes the claim that it will personally investigate the order and send a follow-up. It also removes the unnecessary request for an email address. Instead, it describes what the support team needs to verify. This is a meaningful improvement in operational honesty and instruction adherence. Gemini's answer is also concise and directly relevant.

---

## Cross-Test Analysis

The comparison suggests that a more explicit prompt can influence how models handle conversation history and operational boundaries.

| Dimension | Initial Test | Revised Test |
|---|---|---|
| Context retention | Both models retain the key details | Both continue to retain the key details |
| Operational honesty | Gemini implies access and action | Neither model claims to have acted |
| Information requests | Gemini asks for an email address | Neither model asks for unnecessary information |
| Outcome commitments | Gemini promises an update; GPT mentions possible compensation | Neither promises an update or delivery date; GPT still mentions refund eligibility |
| Concision | GPT is more detailed; Gemini asks an extra question | Both responses are more focused |

These results support a limited conclusion: the revised prompt improved alignment with the desired behavior in this particular scenario. They do not establish that the revised prompt will produce the same improvement in every conversation or across all models.

---

## Key Lessons

1. **Conversation history must be operationally useful:** Retaining a customer's order number is not enough. A reliable chatbot must also use the delivery date, selected service, and additional charge when deciding what information matters in its response.
2. **Context retention is different from capability:** A chatbot can remember every detail while still behaving unreliably. In the initial Gemini output, the model retains the context but speaks as if it can access the shipping carrier and initiate an investigation. A robust prompt should distinguish between explaining what should happen and claiming to have done it.
3. **Explicit constraints can reduce unsupported behavior:** The revised prompt separately addresses system access, completed actions, follow-up promises, refund commitments, and unnecessary questions. This makes the intended boundaries more concrete than a general instruction to respond naturally. However, the GPT output shows that a model can still introduce a specific remedy that approaches a prohibited area without making an outright promise.
4. **Evaluate the actual outputs, not just the prompt:** A revised prompt should be assessed against observable criteria. In this exercise, those criteria include context retention, usefulness, operational honesty, unnecessary requests, and unsupported commitments. A prompt is not successful merely because it sounds more precise. Its outputs must demonstrate the intended behavior.

---

## Limitations

- This is a single customer-support scenario, not a comprehensive evaluation of multi-turn conversation handling.
- The outputs represent observed behavior in these tests; they do not establish consistent performance across repeated runs.
- The exercise does not test whether a chatbot can retrieve real order information or execute a support workflow using connected tools.
- A real deployment would also require testing across different customer intents, missing information, contradictory messages, and escalation cases.

---

## Conclusion

This exercise demonstrates a practical prompt-engineering workflow: establish a baseline, identify observable failure modes, make the instructions more explicit, and compare the resulting outputs against the same criteria.

The main improvement is not simply better wording. It is a clearer boundary between using conversational context, recommending an appropriate next step, and claiming operational capabilities the chatbot has not been given.

**Core takeaway:** Reliable multi-turn chatbots need both context retention and disciplined behavior. Remembering the conversation is necessary, but not sufficient, for trustworthy customer support.
