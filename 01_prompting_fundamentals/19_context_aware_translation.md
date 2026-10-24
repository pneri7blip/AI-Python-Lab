# Context-Aware Translation

## Objective

Evaluate how well a prompt guides different language models to translate a customer support message while preserving meaning, tone, and factual details.

The test focuses on natural professional English, preservation of the customer's frustrated but polite tone, and avoiding unsupported changes to technical details or times.

---

## Initial Prompt

You are a professional localization specialist working on customer support communications for an international technology company.

Translate the following Italian customer message into English.

Requirements:
- Preserve the original meaning and all factual details.
- Maintain the customer's frustrated but polite tone.
- Use natural, professional English suitable for a customer support ticket.
- Preserve technical details, quantities, dates, and product names exactly as stated.
- Do not add explanations, assumptions, apologies, or information that is not present in the original.
- Return only the translated message.

Italian message:

"Ho installato l'aggiornamento ieri sera, ma da stamattina l'app si blocca ogni volta che provo a esportare un report. Ho già riavviato il telefono due volte e il problema si presenta ancora. Mi serve il report entro domani alle 10:00 per una riunione con il cliente. Potete verificare cosa sta succedendo?"

---

## Initial Outputs

### GPT

> I installed the update last night, but since this morning, the app has been crashing every time I try to export a report. I’ve already restarted my phone twice, but the problem persists. I need the report by tomorrow at 10:00 for a meeting with the client. Could you please check what’s going on?

### Gemini

> I installed the update last night, but since this morning the app crashes every time I try to export a report. I have already restarted my phone twice and the problem still occurs. I need the report by tomorrow at 10:00 AM for a client meeting. Could you check what is going on?

---

## Initial Evaluation

Both outputs were fluent, professional, and broadly faithful to the source.

Two differences were worth examining:

- **“si blocca”** was translated as “has been crashing” by GPT and “crashes” by Gemini. Both are plausible, although “crashing” can imply that the application closes or fails, while “freezing” more specifically suggests that it stops responding.
- The source gives the time as **“10:00”**. Gemini changed it to “10:00 AM,” adding an interpretation that was not explicitly stated.

These observations motivated a more explicit prompt revision. They do not establish that either translation is categorically wrong.

---

## Prompt Revision 1

The revised prompt strengthened the instruction not to infer or clarify unstated information and emphasized preserving time expressions as supplied.

You are a professional localization specialist translating customer support communications.

Translate the Italian message into natural, professional English.

Requirements:
- Preserve the original meaning, tone, and all factual details.
- Do not add, infer, or clarify information that is not explicitly stated in the source.
- Preserve dates, times, quantities, and product names exactly as provided, adapting only what is necessary for grammatical English.
- Maintain the customer's frustrated but polite tone.
- Do not add explanations or omit information.
- Return only the translated message.

Italian message:

"Ho installato l'aggiornamento ieri sera, ma da stamattina l'app si blocca ogni volta che provo a esportare un report. Ho già riavviato il telefono due volte e il problema si presenta ancora. Mi serve il report entro domani alle 10:00 per una riunione con il cliente. Potete verificare cosa sta succedendo?"

---

## Revised Outputs

### GPT

> I installed the update last night, but since this morning, the app has been freezing every time I try to export a report. I've already restarted my phone twice, but the problem persists. I need the report by tomorrow at 10:00 for a meeting with the client. Could you please check what's going on?

### Gemini

> I installed the update last night, but since this morning the app crashes every time I try to export a report. I have already restarted my phone twice and the problem still occurs. I need the report by tomorrow at 10:00 AM for a client meeting. Could you check what is going on?

---

## Evaluation

| Criterion | GPT, revised prompt | Gemini, revised prompt |
|---|---|---|
| Meaning broadly preserved | Yes | Yes |
| Natural, professional English | Yes | Yes |
| Customer's polite, concerned tone | Preserved | Preserved |
| Restart count and report deadline retained | Yes | Yes |
| Time retained exactly as `10:00` | Yes | No; output says `10:00 AM` |
| Translation of “si blocca” | “freezing” | “crashes” |

GPT's revised output used “freezing,” a potentially closer match if the Italian means that the app stops responding. The source alone does not confirm the app's exact technical behavior, so the distinction remains contextual.

Gemini's output was effectively unchanged from its initial translation, including the addition of “AM.” The revised instruction therefore did not produce an observable improvement on that detail in this test.

Overall, the first prompt already produced usable translations. The revision improved GPT's handling of the two details under review, but it did not lead to the same change in Gemini. This is a small comparison involving one source message and two models, not evidence of general reliability.

---

## Key Takeaway

Good translation prompts specify more than the target language: they define the expected tone, audience, fidelity, and boundaries on adding information. Comparing outputs against explicit criteria helps identify subtle semantic choices and details that may be changed during translation.

A more detailed instruction does not guarantee better results across every model. For consequential localization workflows, prompts should be tested on multiple examples, including ambiguous phrases and formats such as times and dates, with human review where accuracy matters.
