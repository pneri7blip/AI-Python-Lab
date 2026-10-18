# Topic Matching & Alerting

## Objective

Evaluate whether a language model can match a news report against a predefined list of monitored topics and produce a consistent alert decision.

The exercise tests semantic topic matching, exclusion of unsupported categories, and consistency between a list of matched topics and a boolean alert field.

---

## Initial Prompt

You are assisting a corporate risk-monitoring team.

Analyze the news report and determine whether it matches any of the monitored topics.

Return a valid JSON object with exactly these fields:

- "Matched_Topics": a list containing only monitored topics meaningfully supported by the report
- "Alert": true if at least one monitored topic matches, otherwise false

Monitored topics:
- "cybersecurity"
- "service disruption"
- "supply chain"
- "financial performance"
- "employee satisfaction"

Apply these rules:
- Match topics based on the meaning of the report, not merely isolated keywords.
- Use the monitored topic labels exactly as written.
- Include every monitored topic that is meaningfully supported by the report.
- Do not include topics based on assumptions or outside knowledge.
- Set "Alert" to true if and only if "Matched_Topics" contains at least one topic.
- Return valid JSON only. Do not include explanations or additional fields.

News Report:

"Technology company Vertex Systems disclosed that a software outage disrupted access to its business platform for six hours on Tuesday. The company has launched an investigation after discovering unauthorized access to part of its customer database. Separately, several enterprise customers reported that deliveries of replacement networking equipment were delayed by two weeks because a component supplier missed its shipment deadline. Vertex Systems has not yet released updated financial guidance, and the company said it is still assessing the operational impact of these incidents."

---

## Initial Test: Relevant Topics Present

### GPT-5.6 Luna

> {
>   "Matched_Topics": [
>     "cybersecurity",
>     "service disruption",
>     "supply chain"
>   ],
>   "Alert": true
> }

### Gemini 3.1 Pro

> {
>   "Matched_Topics": [
>     "cybersecurity",
>     "service disruption",
>     "supply chain"
>   ],
>   "Alert": true
> }

---

## Evaluation

Both models selected the same three topics:

- **cybersecurity:** the report describes unauthorized access to a customer database.
- **service disruption:** a software outage interrupted access to the platform.
- **supply chain:** a component supplier missed a shipment deadline, delaying equipment deliveries.

Neither model selected "financial performance", because the report did not provide financial results or a confirmed financial impact. Neither selected "employee satisfaction", which was not meaningfully supported by the report.

Both models returned "Alert: true", consistent with the presence of matched topics.

---

## Control Test: No Monitored Topics Present

To check whether the prompt also avoids unsupported matches, both models were tested with a second report while keeping the original instructions and monitored-topic list unchanged.

### Control Report

"Vertex Systems announced that its design team has completed a new user-interface prototype for its business platform. Employees will be invited to test the layout next month, and the company plans to collect feedback on navigation, accessibility, and visual consistency before deciding whether to proceed with the design. The announcement did not mention security incidents, service outages, supplier problems, financial results, or employee satisfaction."

### GPT-5.6 Luna

> {
>   "Matched_Topics": [],
>   "Alert": false
> }

### Gemini 3.1 Pro

> {
>   "Matched_Topics": [],
>   "Alert": false
> }

---

## Control Evaluation

Both models returned an empty list and "Alert: false". This was consistent with the control report, which described interface design work without providing meaningful evidence for any monitored topic.

The control test provided an initial check against false-positive matches. However, because the report explicitly stated that the monitored issues were not mentioned, this was a relatively easy negative case rather than a difficult ambiguity test.

---

## Overall Evaluation

Across the two test cases, both models produced identical outputs and maintained consistency between "Matched_Topics" and "Alert".

The positive case tested recognition of three supported topics while excluding two unsupported categories. The control case tested whether the models could return no matches and suppress the alert.

These results demonstrate consistent behavior on the examples tested, but they do not establish production-level reliability. A broader evaluation would require more reports, including ambiguous cases, indirect references, mixed signals, and reports that mention a monitored topic only incidentally.

---

## Key Takeaway

Topic matching and alerting combine semantic classification with a downstream decision rule. A reliable prompt must define what counts as meaningful evidence, restrict outputs to predefined labels, and ensure that the alert decision follows the matched-topic list.

Testing both positive and negative cases helps reveal whether a model can identify relevant signals without triggering alerts for unrelated content. In a production workflow, these checks should be supplemented with automated JSON-schema validation and a larger evaluation dataset.
