# Tone Transformation

## Objective

Evaluate how effectively a prompt can transform the tone of a business message while preserving its factual content, main concerns, and requests.

The goal is to make a message more diplomatic and professional without weakening its meaning or introducing unsupported information.

---

## Initial Prompt

You are a professional business communication editor.

Rewrite the following message to make it more diplomatic and professional while preserving its original meaning.

Requirements:
- Keep all factual details and commitments unchanged.
- Preserve the sender's main concern and request.
- Replace accusatory or emotionally charged wording with constructive language.
- Do not make the message overly apologetic or excessively formal.
- Do not invent explanations, promises, deadlines, or new requests.
- Keep the message concise and natural.
- Return only the rewritten message.

Original message:

"I'm tired of asking for the same update. Nobody has told me what's happening, and this delay is putting our work at risk. I need a clear answer today about when this will be finished."

---

## Initial Outputs

### GPT

> «I’d appreciate an update on the current status, as I haven’t yet received clarity on the progress. The delay is putting our work at risk, so I need a clear response today confirming when this will be completed.»

### Gemini

> «I'm following up to request an update on this item. As the ongoing delay is beginning to impact our workflow, could you please provide a clear completion date by the end of today?»

---

## Initial Evaluation

Both models transformed the original message into professional business communication, but they made different choices.

- GPT preserved the explicit statement that the delay was putting the work at risk and retained the request for a clear answer today.
- Gemini produced a concise and polite message, but changed the risk statement to an impact on the workflow. The phrase "beginning to impact" also introduces a nuance not explicitly present in the source.
- Both models removed the direct expression of frustration in the original message.
- Gemini requested a clear completion date, while the original asked for a clear answer about when the work would be finished. These are closely related, but not identical.

The initial outputs suggested that the prompt could be more explicit about preserving substantive meaning while changing the tone.

---

## Prompt Revision 1

The revised prompt specifically requires the models to retain the risk to the work and the request for an answer today.

You are a professional business communication editor.

Rewrite the message to make it more diplomatic and professional without weakening or changing its substantive meaning.

Requirements:
- Preserve every important concern, fact, request, and deadline from the original.
- Retain the explicit statement that the delay is putting the work at risk.
- Preserve the request for a clear answer today about when the work will be completed.
- Replace expressions of frustration or blame with constructive, professional wording, without removing the underlying concern.
- Do not introduce new claims, assumptions, commitments, or deadlines.
- Keep the message concise and natural.
- Return only the rewritten message.

Original message:

"I'm tired of asking for the same update. Nobody has told me what's happening, and this delay is putting our work at risk. I need a clear answer today about when this will be finished."

---

## Revised Outputs

### GPT

> «I’m following up again as I have not yet received an update on the current status. The lack of clarity, combined with the ongoing delay, is putting our work at risk. Please provide a clear answer today confirming when this work will be completed.»

### Gemini

> «I am following up again as I have not yet received an update. This delay is putting our work at risk, and I need a clear answer today about when this will be finished.»

---

## Evaluation

| Criterion | GPT, revised prompt | Gemini, revised prompt |
|---|---|---|
| Professional and diplomatic tone | Yes | Yes |
| Explicitly preserves the risk to the work | Yes | Yes |
| Requests a clear answer today | Yes | Yes |
| Retains the request for completion timing | Yes | Yes |
| Removes direct expressions of frustration | Yes | Yes |
| Preserves the lack-of-update concern | Explicitly mentions status and lack of clarity | Mentions the lack of an update |

The revised prompt produced outputs that more explicitly preserved the central concern and deadline.

GPT retained both the lack of clarity and the ongoing delay as separate reasons for concern. Gemini was more concise and preserved the core message, although it omitted the separate reference to the lack of clarity.

The results suggest that explicit preservation requirements helped guide both models toward the intended message. However, this is a small test using one source message and two models; it does not establish that the revised prompt will always perform better.

---

## Key Takeaway

Tone transformation is not simply about making language sound more polite. A successful rewrite must preserve the message's important facts, concerns, urgency, and requested action.

Explicitly identifying what must not change can help reduce the risk of over-softening a message or altering its meaning. Different models may still omit or emphasize details differently, so outputs should be evaluated against clear criteria rather than judged on style alone.
