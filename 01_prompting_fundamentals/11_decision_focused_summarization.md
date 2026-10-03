# Decision-Focused Summarization

## Objective

Explore how a summarization prompt can direct an AI model to prioritize information relevant to a specific purchasing criterion while excluding less relevant details.

## Prompt Used

You are assisting a procurement analyst.

Summarize the vendor information below in no more than 70 words.

Focus only on:
- pricing and costs
- contract conditions
- operational value
- limitations that could affect the purchasing decision

Ignore technical specifications that are not relevant to these areas.

Do not add information that is not explicitly stated in the source.

Vendor A — ClearFlow Analytics

ClearFlow offers an annual subscription of €8,400 with no setup fee. The contract can be cancelled with 30 days' notice. The package includes unlimited users and email support during business hours.

The platform processes up to 50,000 records per month. Additional records cost €0.08 per record.

Vendor B — DataBridge Solutions

DataBridge offers an annual subscription of €6,000 with a one-time setup fee of €2,500. The contract requires a minimum commitment of 24 months.

The package includes up to 10 users and priority email support. Additional users cost €40 per user per month.

DataBridge includes up to 100,000 processed records per month with no additional per-record charge.

Both vendors provide automated reporting and dashboard functionality.

---

## Input Text

Vendor A — ClearFlow Analytics

ClearFlow offers an annual subscription of €8,400 with no setup fee. The contract can be cancelled with 30 days' notice. The package includes unlimited users and email support during business hours.

The platform processes up to 50,000 records per month. Additional records cost €0.08 per record.

Vendor B — DataBridge Solutions

DataBridge offers an annual subscription of €6,000 with a one-time setup fee of €2,500. The contract requires a minimum commitment of 24 months.

The package includes up to 10 users and priority email support. Additional users cost €40 per user per month.

DataBridge includes up to 100,000 processed records per month with no additional per-record charge.

Both vendors provide automated reporting and dashboard functionality.

---

## Model Outputs

### GPT-5.6 Luna

> ClearFlow Analytics: €8,400/year, no setup fee; cancellable with 30 days’ notice. Unlimited users and business-hours email support. Includes 50,000 records/month; additional records cost €0.08 each.
>
> DataBridge Solutions: €6,000/year plus €2,500 setup; 24-month minimum commitment. Includes 10 users and priority email support; additional users cost €40/month. Includes 100,000 records/month with no per-record charge.
>
> Both provide automated reporting and dashboards.

### Gemini 3.1 Pro

> ClearFlow: €8,400/yr, €0 setup, flexible 30-day cancellation. Includes unlimited users and business-hour support, but is limited to 50,000 records/month (extras cost €0.08/record).
>
> DataBridge: €6,000/yr, €2,500 setup, strict 24-month commitment. Includes up to 100,000 records/month and priority support, but limits access to 10 users (extras cost €40/month).
>
> Operational Value: Both platforms provide automated reporting and dashboards.

---

## Evaluation

Tested with two LLMs (GPT-5.6 Luna and Gemini 3.1 Pro) to evaluate focused summarization and information prioritization.

Both models stayed within the 70-word constraint and retained the key information related to pricing, contract conditions, operational value, and relevant limitations.

Gemini used a more compressed structure and explicitly grouped the shared reporting and dashboard functionality under "Operational Value." GPT-5.6 Luna preserved more of the original wording and included the vendors' full names.

Neither model introduced a purchasing recommendation or information that was not present in the source. The comparison shows that the same summarization constraints can lead different models to compress and prioritize information in slightly different ways.

---

## Key Takeaway

Focused summarization can be used to tailor a summary to a specific decision criterion rather than treating all source information as equally important.

This experiment also shows that different LLMs may use different compression and prioritization strategies while still satisfying the same instructions and preserving the key information required by the task.
