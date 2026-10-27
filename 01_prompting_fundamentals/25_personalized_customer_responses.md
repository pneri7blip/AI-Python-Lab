# Personalized Customer Responses

## Objective

Explore how an AI model can generate personalized customer support responses using a customer review, its sentiment, and explicit writing instructions.

The exercise focuses on three practical requirements:

- Acknowledge the customer's actual experience.
- Provide a useful next step.
- Avoid promising actions or outcomes that have not been authorized or verified.

---

## Initial Prompt

You are a customer support representative for an online store.

Write a response to the following customer review.

Review sentiment: negative

Customer review: "The blender arrived two days late. When it finally arrived, the motor made a loud noise and stopped working after a few minutes. I contacted support but haven't received a reply yet."

Write a concise, empathetic response that acknowledges the customer's specific problems and offers a reasonable next step. Do not claim that a refund, replacement, or other action has already been approved. Avoid generic apologies that could apply to any review.

The same prompt was tested with GPT and Gemini.

---

## Initial Results

### GPT

> «We’re sorry your blender arrived two days late and then developed a loud motor noise before stopping working. We also understand how frustrating it is to have contacted support and still be waiting for a response. Please contact our customer support team with your order number so we can review the issue and help arrange an appropriate solution. Thank you for your patience, and we apologize for the inconvenience.»

### Gemini

> «Hi there,
> I am so sorry for the frustrating experience you've had. Waiting two days longer than expected for your blender, only for the motor to break down after just a few minutes—and then experiencing a delay in hearing back from our support team—is certainly not the level of service we want to provide.
> I want to get this sorted out for you immediately. Could you please reply with your order number? I will personally locate your previous message, escalate your case, and follow up with you shortly with the next steps for a replacement or refund.
> Thank you for your patience, and I look forward to making this right for you.
> Best regards,
> [Your Name]
> Customer Support Team»

---

## Initial Observations

Both models acknowledged the main problems and proposed a next step.

However, Gemini went beyond the information and capabilities established in the prompt. It claimed that it would locate a previous message, escalate the case, follow up shortly, and provide next steps for a replacement or refund.

These statements sound helpful, but they imply operational capabilities and future actions that were not established.

GPT avoided these specific promises, although its response was less personal.

---

## Revised Prompt

The second version makes the boundaries of the assistant's role more explicit.

You are a customer support writing assistant for an online store.

Write a concise, empathetic reply to the following customer review.

Review sentiment: negative

Customer review:
"The blender arrived two days late. When it finally arrived, the motor made a loud noise and stopped working after a few minutes. I contacted support but haven't received a reply yet."

Requirements:
- Acknowledge the delivery delay, the motor failure, and the unanswered support request.
- Apologize sincerely without exaggerating or repeating the same apology.
- Suggest one clear, reasonable next step.
- Do not claim that you have accessed an order, located a previous message, contacted another team, escalated a case, or initiated any action.
- Do not promise a response time, replacement, refund, or other outcome.
- Do not invent facts or imply that an action has already been taken.
- Use a professional, natural tone.
- Output only the customer-facing reply.

---

## Results After Prompt Revision

### GPT

> «We’re sorry your blender arrived late, stopped working after just a few minutes, and that you haven’t received a reply from our support team. We understand how frustrating and disappointing this experience must be. Please reply to your original support request with a brief description of the motor issue so your concern can be reviewed. Thank you for your patience, and we apologize for the inconvenience.»

### Gemini

> «Dear Customer,
> Thank you for reaching out and sharing your feedback. I am truly sorry to hear that your blender arrived two days late, experienced a motor failure right after startup, and that your initial message to our support team went unanswered. This is certainly not the experience we aim to provide.
> To help us address this issue promptly, please reply directly with your order number or the email address associated with your purchase. Once we have those details, a team member will review your situation and work with you on a solution.
> Best regards,
> Customer Support Team»

---

## Comparative Evaluation

| Criterion | GPT: Initial | GPT: Revised | Gemini: Initial | Gemini: Revised |
|---|---|---|---|---|
| Acknowledges specific problems | Yes | Yes | Yes | Yes |
| Shows empathy | Yes | Yes | Yes | Yes |
| Suggests a next step | Yes | Yes | Yes | Yes |
| Avoids explicit unsupported operational promises | Yes | Yes | No | Improved, but incomplete |
| Follows the prompt's constraints | Mostly | Mostly | Partially | Partially |

### GPT: What Changed?

GPT remained cautious in both tests. Its revised response suggests replying to the original support request, which is a reasonable next step.

One limitation remains: asking the customer to describe the motor issue again may be unnecessary, since the issue is already described in the review. The prompt does not explicitly require the next step to avoid requesting information already available.

### Gemini: What Changed?

Gemini no longer claims that it will personally locate the previous message, escalate the case, and follow up shortly.

However, it still states that a team member will review the situation and work toward a solution. This is a future operational commitment that the prompt did not establish as guaranteed.

The revised prompt therefore reduced some unsupported commitments but did not eliminate all of them.

---

## Key Learnings

1. **Specificity is not enough:** A response can accurately repeat details from a review while still making unsupported claims about what happens next.
2. **Constraints need to cover implied commitments:** Prohibiting promises of refunds or replacements does not automatically prevent a model from promising escalation, follow-up, or action by another team.
3. **Prompt improvements must be tested:** The revised prompt produced a more constrained Gemini response, but some overcommitment remained. The improvement is partial rather than complete.
4. **Helpfulness and reliability must be evaluated together:** A response that sounds proactive may create false expectations. Conversely, an overly cautious response may fail to give the customer a useful next step.

The goal is to balance empathy, specificity, practical usefulness, and factual restraint.

---

## Limitations

This experiment used one customer review and one initial/revised prompt pair, tested with two models.

The findings are exploratory. They do not establish that one model is generally more reliable than the other, or that the revised prompt will work better across other reviews and customer support scenarios.

A more robust evaluation would use a representative set of reviews, predefined evaluation criteria, and examples covering different product failures, billing issues, delivery problems, and requests for refunds.

For deployment, customer-facing messages should also be checked against the organization's actual support policies and available operational capabilities.

---

## Conclusion

This exercise demonstrates how prompt constraints can shape AI-generated customer responses and reduce unsupported operational commitments.

The central lesson is that a useful customer support prompt should specify not only what the model must communicate, but also what it must not claim to have done or be able to guarantee.

Prompt engineering is an iterative process: define requirements, test outputs, identify failure modes, refine constraints, and evaluate the results again.
