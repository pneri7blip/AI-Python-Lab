# AI Project Update Summarization

## Objective

Explore how summarization constraints can help an AI model transform a detailed project update into a concise and actionable briefing.

## Prompt Used

Your task is to assist a project consultant.

Summarize the project update below in no more than 50 words.

Focus on:
- major developments
- problems or risks
- actions that require attention

Do not add information that is not present in the source.

Project Update — Riverside Office Renovation

The electrical installation on the second floor has been completed, while work on the first floor is approximately 70% complete.

During the latest inspection, the team identified damaged electrical cables in two areas of the first floor. The affected cables must be replaced before the electrical work can continue in those areas.

The delivery of the new ventilation units has been delayed by approximately one week due to a supplier issue. This may affect the planned installation schedule.

The construction team has also requested confirmation of the final lighting layout before completing the ceiling work.

The project remains within the current budget, but the schedule may require adjustment if the ventilation delay continues.

---

## Input Text

Project Update — Riverside Office Renovation

The electrical installation on the second floor has been completed, while work on the first floor is approximately 70% complete.

During the latest inspection, the team identified damaged electrical cables in two areas of the first floor. The affected cables must be replaced before the electrical work can continue in those areas.

The delivery of the new ventilation units has been delayed by approximately one week due to a supplier issue. This may affect the planned installation schedule.

The construction team has also requested confirmation of the final lighting layout before completing the ceiling work.

The project remains within the current budget, but the schedule may require adjustment if the ventilation delay continues.

---

## Model Outputs

### GPT-5.6 Luna

> Second-floor electrical work is complete; first-floor work is 70% complete. Damaged cables must be replaced before affected areas can proceed. Ventilation-unit delivery is delayed by one week, potentially affecting the schedule. Final lighting layout confirmation is needed before ceiling work. Budget remains on track.

### Gemini 3.1 Pro

> Project Update Summary:
> Second-floor electrical work is complete; the first floor is 70% done but requires replacing damaged cables. A one-week delay in receiving ventilation units threatens the overall schedule. Action required: Confirm the final lighting layout so the construction team can finish the ceiling work.

---

## Evaluation

Tested with two LLMs (GPT-5.6 Luna and Gemini 3.1 Pro) to evaluate prompt portability and consistency.

Both models followed the 50-word constraint and captured the main project developments, risks, and required actions.

GPT-5.6 Luna retained the information that the project remained within budget. Gemini omitted this detail and described the schedule impact more strongly than the source, using the phrase "threatens the overall schedule" instead of the more cautious wording ("may affect") used in the original text.

Overall, both models produced concise and relevant summaries, but the comparison highlights how different models may prioritize information and vary in how closely they preserve the source's wording and level of certainty.

---

## Key Takeaway

Effective summarization prompts do more than ask a model to shorten text. Explicit constraints can define the desired length, focus, and relationship to the original source.

This experiment also shows that different LLMs may prioritize different information or express the same source information with different levels of certainty, making output evaluation an important part of prompt development.
