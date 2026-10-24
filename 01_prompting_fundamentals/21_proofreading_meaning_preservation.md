# Proofreading with Meaning Preservation

## Objective

Evaluate whether a language model can correct grammar, spelling, punctuation, and word usage while preserving the author's original meaning, tone, and factual claims.

The exercise focuses on minimal editing: correcting genuine errors without unnecessarily rewriting correct sentences or changing the level of certainty expressed in the source.

---

## Initial Prompt

You are a professional English proofreader.

Correct the grammar, spelling, punctuation, and wording errors in the following message.

Requirements:
- Preserve the author's original meaning and intent.
- Keep the original tone and level of formality.
- Make only the changes necessary to correct errors and improve clarity.
- Do not add new information, remove details, or change factual claims.
- Do not rewrite correct sentences just to make them sound different.
- Return only the corrected message.

Text to proofread:

"Hi team, I wanted to let you know that the client have reviewed the latest version and they was happy with most of the changes. However, they has requested two additional adjustment before we can considers the project completed. I will send the details tomorrow, because I haven't received all the informations yet."

---

## Initial Outputs

### GPT

> «Hi team, I wanted to let you know that the client has reviewed the latest version and they were happy with most of the changes. However, they have requested two additional adjustments before we can consider the project completed. I will send the details tomorrow because I haven't received all the information yet.»

### Gemini

> «Hi team, I wanted to let you know that the client has reviewed the latest version and they were happy with most of the changes. However, they have requested two additional adjustments before we can consider the project completed. I will send the details tomorrow, because I haven't received all the information yet.»

---

## Initial Evaluation

Both models corrected the grammatical errors and preserved the original meaning.

The corrections included:

- "the client have" → "the client has"
- "they was" → "they were"
- "they has requested" → "they have requested"
- "two additional adjustment" → "two additional adjustments"
- "we can considers" → "we can consider"
- "all the informations" → "all the information"

The only minor difference was punctuation: GPT omitted the comma before "because," while Gemini retained it. Both outputs remained understandable and natural.

The initial test showed that both models could correct the obvious errors, but a second test was needed to examine whether they would avoid unnecessary changes and preserve uncertainty.

---

## Prompt Revision 1

The revised prompt explicitly requires minimal editing and preservation of factual certainty.

You are a professional English proofreader.

Correct only genuine errors in grammar, spelling, punctuation, or word usage in the text below.

Requirements:
- Preserve the author's original meaning, intent, tone, and level of formality.
- Make the smallest changes necessary to correct genuine errors.
- Do not rewrite sentences that are already grammatically correct, even if you could make them more elegant or concise.
- Do not add, remove, or infer factual information.
- Preserve all dates, quantities, commitments, and degrees of certainty.
- Return only the corrected text.

Text to proofread:

"Hi team, the client have reviewed the latest version and they were happy with most of the changes. They asked us to make two additional adjustments, which should be fairly easy to complete. I think we can probably finish them by Friday, but this hasn't been confirmed yet."

---

## Revised Outputs

### GPT

> «Hi team, the client has reviewed the latest version and they were happy with most of the changes. They asked us to make two additional adjustments, which should be fairly easy to complete. I think we can probably finish them by Friday, but this hasn't been confirmed yet.»

### Gemini

> «Hi team, the client has reviewed the latest version and they were happy with most of the changes. They asked us to make two additional adjustments, which should be fairly easy to complete. I think we can probably finish them by Friday, but this hasn't been confirmed yet.»

---

## Evaluation

Both models returned exactly the same corrected text.

The genuine grammatical error was corrected:

- "the client have" → "the client has"

The rest of the message was preserved, including:

- The statement that the client was happy with most of the changes.
- The assessment that the additional adjustments should be fairly easy.
- The tentative estimate that the work could probably be completed by Friday.
- The explicit statement that the completion estimate had not yet been confirmed.

Neither model turned the tentative estimate into a firm commitment, added facts, or unnecessarily rewrote the correct sentences.

The revised test therefore provided evidence that both models followed the minimal-editing requirement on this particular example. Identical outputs do not, by themselves, establish that the models will behave identically on other texts.

---

## Key Takeaway

Effective proofreading requires more than grammatical accuracy. A model must also preserve the author's meaning, tone, factual details, and degree of certainty.

Explicit instructions to make minimal changes can help distinguish proofreading from rewriting. For professional evaluation, the corrected text should be checked not only for remaining errors, but also for unintended changes to the original message.

This test involved one initial example and one revised example across two models. Broader testing would be needed to evaluate reliability across different writing styles and error types.
