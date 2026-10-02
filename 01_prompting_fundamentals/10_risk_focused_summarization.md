# Risk-Focused Report Summarization

## Objective

Explore how a summarization prompt can direct an AI model to focus on specific information within a larger document while ignoring irrelevant details.

## Prompt Used

You are assisting an environmental compliance consultant.

Summarize the inspection report below in no more than 60 words.

Focus only on:
- compliance risks
- identified issues or non-conformities
- actions that require attention

Ignore general project information that is not relevant to these areas.

Do not add information that is not explicitly stated in the report.

Inspection Report — Northfield Manufacturing Facility

The facility employs 86 people and operates Monday through Friday. Production has increased by approximately 12% compared with the previous quarter.

During the inspection, three containers of chemical waste were found without the required identification labels. The containers were stored in the designated hazardous-waste area.

The facility's emergency response plan was last updated eight months ago. The inspection team recommended reviewing the plan to ensure that it reflects the current site layout.

All fire extinguishers inspected were within their service dates.

One drainage channel near the loading area contained accumulated sediment and debris. The inspection team recommended cleaning the channel and checking it regularly.

The facility's waste transfer records were complete and available for inspection.

No evidence of unauthorized discharge was identified during the inspection.

---

## Input Text

Inspection Report — Northfield Manufacturing Facility

The facility employs 86 people and operates Monday through Friday. Production has increased by approximately 12% compared with the previous quarter.

During the inspection, three containers of chemical waste were found without the required identification labels. The containers were stored in the designated hazardous-waste area.

The facility's emergency response plan was last updated eight months ago. The inspection team recommended reviewing the plan to ensure that it reflects the current site layout.

All fire extinguishers inspected were within their service dates.

One drainage channel near the loading area contained accumulated sediment and debris. The inspection team recommended cleaning the channel and checking it regularly.

The facility's waste transfer records were complete and available for inspection.

No evidence of unauthorized discharge was identified during the inspection.

---

## Model Outputs

### GPT-5.6 Luna

> Three chemical-waste containers lacked required identification labels; corrective labeling is required.
>
> Emergency response plan should be reviewed to ensure it reflects the current site layout.
>
> Drainage channel near the loading area requires cleaning and regular inspection due to accumulated sediment and debris.

### Gemini 3.1 Pro

> Key issues requiring attention:
>
> Unlabeled Waste: Three chemical waste containers in the hazardous-waste area lack required identification labels.
>
> Emergency Plan: The emergency response plan must be reviewed and updated to reflect the current site layout.
>
> Drainage Maintenance: A drainage channel near the loading area contains accumulated sediment and debris, requiring cleaning and regular monitoring.

---

## Evaluation

Tested with two LLMs (GPT-5.6 Luna and Gemini 3.1 Pro) to evaluate focused summarization and source fidelity.

Both models stayed within the 60-word constraint and correctly identified the three issues requiring attention while omitting unrelated information from the report (such as headcount, production metrics, and positive compliance findings).

GPT-5.6 Luna preserved the level of certainty used in the source. Gemini, however, strengthened one recommendation by describing the emergency response plan as something that "must be reviewed and updated," whereas the source only recommended reviewing it.

This highlights how focused summarization can successfully prioritize relevant information while still requiring evaluation for changes in the strength or certainty of the original statements.

---

## Key Takeaway

Focused summarization allows a model to prioritize specific information instead of treating every part of a source document as equally important.

This experiment also demonstrates the importance of source fidelity: a summary can contain the correct facts while subtly changing the strength or certainty of the original statements.
