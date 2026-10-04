# Source-Based Information Extraction

## Objective

Explore how structured extraction instructions can help an AI model identify specific information from a source document while preserving source fidelity and avoiding unsupported inferences.

## Prompt Used

You are assisting an environmental compliance consultant.

Extract only the compliance risks identified in the inspection report below.

For each risk, provide:
- Risk
- Evidence
- Required Action

Use only information explicitly stated in the report.
Do not infer additional risks or actions.

If a field is not specified in the report, write: "Not specified."

Inspection Report — Westbrook Processing Facility

During a routine inspection, two containers of solvent waste were found without the required hazard labels. The containers were located in the designated hazardous-waste storage area.

The facility's emergency response plan was last reviewed 14 months ago. The inspection team recommended reviewing the plan to ensure that it remains aligned with current emergency procedures.

A secondary containment area near the chemical storage zone contained approximately 5 cm of standing water. The inspection report recommends removing the water and checking the containment area for possible drainage problems.

All hazardous-waste transfer records reviewed during the inspection were complete.

The facility's air-emissions monitoring equipment was operating within the required calibration period.

No unauthorized chemical discharge was observed during the inspection.

---

## Input Text

Inspection Report — Westbrook Processing Facility

During a routine inspection, two containers of solvent waste were found without the required hazard labels. The containers were located in the designated hazardous-waste storage area.

The facility's emergency response plan was last reviewed 14 months ago. The inspection team recommended reviewing the plan to ensure that it remains aligned with current emergency procedures.

A secondary containment area near the chemical storage zone contained approximately 5 cm of standing water. The inspection report recommends removing the water and checking the containment area for possible drainage problems.

All hazardous-waste transfer records reviewed during the inspection were complete.

The facility's air-emissions monitoring equipment was operating within the required calibration period.

No unauthorized chemical discharge was observed during the inspection.

---

## Model Outputs

### GPT-5.6 Luna

> **Risk 1**
> - **Risk:** Solvent waste containers lacked required hazard labels.
> - **Evidence:** Two containers of solvent waste were found without the required hazard labels in the designated hazardous-waste storage area.
> - **Required Action:** Not specified.
>
> **Risk 2**
> - **Risk:** Emergency response plan may need review.
> - **Evidence:** The plan was last reviewed 14 months ago.
> - **Required Action:** Review the plan to ensure that it remains aligned with current emergency procedures.
>
> **Risk 3**
> - **Risk:** Standing water in the secondary containment area.
> - **Evidence:** Approximately 5 cm of standing water was found in a secondary containment area near the chemical storage zone.
> - **Required Action:** Remove the water and check the containment area for possible drainage problems.

### Gemini 3.1 Pro

> **Risk 1**
> - **Risk:** Missing hazard labels on solvent waste containers
> - **Evidence:** Two containers of solvent waste were found without the required hazard labels in the designated hazardous-waste storage area.
> - **Required Action:** Not specified.
>
> **Risk 2**
> - **Risk:** Outdated emergency response plan review
> - **Evidence:** The facility's emergency response plan was last reviewed 14 months ago.
> - **Required Action:** Review the plan to ensure that it remains aligned with current emergency procedures.
>
> **Risk 3**
> - **Risk:** Standing water in secondary containment area
> - **Evidence:** A secondary containment area near the chemical storage zone contained approximately 5 cm of standing water.
> - **Required Action:** Remove the water and check the containment area for possible drainage problems.

---

## Evaluation

Tested with two LLMs (GPT-5.6 Luna and Gemini 3.1 Pro) to evaluate structured information extraction and source fidelity.

Both models identified the three compliance issues and correctly extracted the supporting evidence and explicitly stated actions. Both models also correctly used "Not specified" where the report did not provide a required action (demonstrating resistance to hallucinating or inferring obvious missing actions like "label the containers").

A minor difference appeared in the description of the emergency response plan. Gemini described the review status as "outdated," introducing an evaluative judgment not explicitly stated in the source text (which only noted that the plan was last reviewed 14 months ago). GPT-5.6 Luna used the more cautious wording "may need review." Both models nevertheless preserved the explicitly stated recommendation to review the plan.

The results show that structured extraction improves output consistency, but individual risk descriptions may still require review to ensure that the model does not convert factual statements into interpretive labels.

---

## Key Takeaway

Structured extraction allows an AI model to retrieve specific information from a document and organize it into a predefined schema.

This experiment demonstrates the importance of distinguishing explicit facts from interpretation. Even when the extracted evidence and required actions are fully accurate, a model may introduce stronger, value-laden wording when summarizing the underlying issue name.
