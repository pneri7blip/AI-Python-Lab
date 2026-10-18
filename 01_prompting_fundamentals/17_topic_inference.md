# Topic Inference

## Objective

Evaluate how prompt instructions affect a model's ability to identify the main topics of a news report.

The exercise focuses on distinguishing central themes from supporting details, avoiding overlapping labels, and maintaining a consistent level of abstraction.

---

## Initial Prompt

You are assisting a content analysis team.

Read the following news report and identify its main topics.

Return a valid JSON object with exactly these fields:

- "Topics": a list of three to five concise topic labels.

Apply these rules:
- Identify the main subjects discussed in the report, not just individual facts or keywords.
- Use concise topic labels that accurately represent the content.
- Include a topic only if it is meaningfully supported by the report.
- Do not introduce topics based on outside knowledge or assumptions.
- Avoid duplicate or overlapping labels.
- Return the topics in order of importance, from most central to least central.
- Return valid JSON only. Do not include explanations or additional fields.

News Report:

"The National Space Agency reported that 95% of its employees were satisfied with their working conditions in its latest internal survey. The agency credited flexible schedules, improved research facilities, and clearer career-development pathways for the result. In contrast, a survey conducted by the Social Security Administration found that only 45% of its employees were satisfied, with respondents citing outdated internal systems and limited opportunities for advancement. Both agencies have pledged to review employee feedback and publish improvement plans next quarter. The findings have renewed discussion about employee satisfaction across federal government agencies."

---

## Initial Outputs

### GPT-5.6 Luna

> {
>   "Topics": [
>     "Employee Satisfaction",
>     "Federal Government Workplace Conditions",
>     "Employee Feedback and Improvement Plans",
>     "Career Development Opportunities",
>     "Workplace Systems and Research Facilities"
>   ]
> }

### Gemini 3.1 Pro

> {
>   "Topics": [
>     "Employee Satisfaction",
>     "Federal Government Workplace Conditions",
>     "Employee Feedback and Improvement Plans",
>     "Career Development Opportunities",
>     "Workplace Systems and Research Facilities"
>   ]
> }

---

## Issue Identified

Both models returned identical topic labels, demonstrating strong agreement on the initial task.

However, the five labels were not all at the same conceptual level:

- "Employee Satisfaction" represented the central theme.
- "Federal Government Workplace Conditions" substantially overlapped with the broader employee-satisfaction theme.
- "Employee Feedback and Improvement Plans" described the agencies' planned response.
- "Career Development Opportunities" represented one factor affecting satisfaction.
- "Workplace Systems and Research Facilities" combined two different supporting details into a broad, somewhat vague label.

The initial prompt asked the models to avoid overlap but did not sufficiently explain how to distinguish broad themes from supporting examples.

---

## Prompt Revision 1

The revised prompt explicitly emphasized broad themes, consistent abstraction, and the distinction between central topics and supporting details.

You are assisting a content analysis team.

Read the following news report and identify its main topics.

Return a valid JSON object with exactly this field:
- "Topics": a list of three to five concise topic labels.

Apply these rules:
- Identify the central subjects of the report, not merely every subject or detail mentioned.
- Prefer broad themes that summarize substantial parts of the report over narrow examples, individual factors, or supporting details.
- Treat specific examples, such as workplace facilities, career opportunities, and internal systems, as supporting details unless they are substantial topics in their own right.
- Keep all topic labels at a consistent level of abstraction.
- Avoid labels that substantially overlap or describe the same underlying topic.
- Include a topic only when it is meaningfully supported by the report.
- Do not introduce topics based on outside knowledge or assumptions.
- Order topics from most central to least central.
- Return valid JSON only. Do not include explanations or additional fields.

News Report:

"The National Space Agency reported that 95% of its employees were satisfied with their working conditions in its latest internal survey. The agency credited flexible schedules, improved research facilities, and clearer career-development pathways for the result. In contrast, a survey conducted by the Social Security Administration found that only 45% of its employees were satisfied, with respondents citing outdated internal systems and limited opportunities for advancement. Both agencies have pledged to review employee feedback and publish improvement plans next quarter. The findings have renewed discussion about employee satisfaction across federal government agencies."

---

## Revised Outputs

### GPT-5.6 Luna

> {
>   "Topics": [
>     "Employee Satisfaction",
>     "Federal Government Workplace Conditions",
>     "Employee Feedback and Organizational Improvement"
>   ]
> }

### Gemini 3.1 Pro

> {
>   "Topics": [
>     "Federal Government Employee Satisfaction",
>     "Agency Workplace Survey Results",
>     "Employee Feedback and Action Plans"
>   ]
> }

---

## Evaluation

The revision reduced the number of topics from five to three in both models. Both outputs removed the separate references to career opportunities, internal systems, and research facilities, treating these as supporting details rather than independent topics.

The revised labels also showed less fragmentation, although the models did not select exactly the same topics:

- GPT retained workplace conditions as a broad theme and described the agencies' response as organizational improvement.
- Gemini explicitly highlighted survey results, emphasizing how the findings were obtained and reported.
- Both retained employee feedback and the planned response as a distinct topic.

The results suggest that clearer instructions can reduce excessive topic extraction. However, agreement on the number of topics does not guarantee agreement on which topics are most important. The appropriate labels depend on the intended classification standard and the purpose of the analysis.

---

## Key Takeaway

Topic inference requires more than extracting keywords or listing every subject mentioned in a text. A useful prompt establishes the desired level of abstraction, prioritizes central themes, and distinguishes them from supporting details.

Comparing model outputs before and after a prompt revision helps reveal whether the instructions reduce redundancy and improve conceptual consistency. Evaluation should consider both the quality of individual labels and the overall coverage of the source.
