# Context-Grounded Content Generation

## Objective

Explore how an AI model can transform source information into a professional status update while preserving factual accuracy, completeness, and appropriate uncertainty.

The exercise focuses on:

- Grounding generated content in provided information.
- Identifying important facts and limitations.
- Distinguishing observed results from assumptions.
- Using explicit structure and constraints to improve consistency.

---

## Initial Prompt

You are an AI assistant helping a project team communicate progress to a manager.

Based only on the project notes below, write a concise professional status update.

Project notes:
- The document-processing prototype can extract invoice numbers, dates, and totals from standard PDF invoices.
- In an initial test of 40 invoices, 34 were processed correctly without manual correction.
- The remaining 6 invoices contained either low-quality scans or unusual layouts.
- The team has not yet tested handwritten invoices.
- The next planned step is to evaluate the prototype on a larger and more varied dataset.
- No production deployment date has been agreed.

Write a clear update that explains current progress, the main limitation, and the next step. Use specific details from the notes. Do not invent facts.

The prompt was tested with GPT and Gemini.

---

## Initial Results

### GPT

> «Project Status Update: Document-Processing Prototype  
> 
> The document-processing prototype can successfully extract invoice numbers, dates, and totals from standard PDF invoices. In an initial test of 40 invoices, 34 were processed correctly without manual correction (85%).  
> 
> The main limitation is that 6 invoices required further attention due to low-quality scans or unusual layouts. Handwritten invoices have not yet been tested, so the prototype’s performance on these remains unknown.  
> 
> Next step: Evaluate the prototype using a larger, more varied dataset to assess its accuracy and identify areas for improvement. No production deployment date has been agreed, and further testing will help inform future readiness decisions.»

### Gemini

> «Project Status Update: Document-Processing Prototype  
> 
> - Current Progress: The prototype successfully extracts invoice numbers, dates, and totals from standard PDF invoices. In an initial test of 40 invoices, 34 were processed correctly without requiring manual correction.  
> - Main Limitations: The remaining 6 invoices contained low-quality scans or unusual layouts, and handwritten invoices have not yet been tested. Additionally, no production deployment date has been agreed upon.  
> - Next Step: Evaluate the prototype on a larger and more varied dataset.»

---

## Initial Evaluation

Both models preserved the key facts and produced coherent professional updates.

- **GPT** calculated the initial success rate of 85% and explicitly connected further testing to future readiness decisions.
- **Gemini** used a concise, scannable structure but did not calculate the percentage.

Neither response invented a deployment date or claimed that the prototype was ready for production.

The initial results were already useful, so the next iteration focused on consistency and explicit output requirements rather than correcting a major factual error.

---

## Revised Prompt

You are an AI assistant preparing project updates for business managers.

Use only the project notes provided below.

Project notes:
- The document-processing prototype can extract invoice numbers, dates, and totals from standard PDF invoices.
- In an initial test of 40 invoices, 34 were processed correctly without manual correction.
- The remaining 6 invoices contained either low-quality scans or unusual layouts.
- The team has not yet tested handwritten invoices.
- The next planned step is to evaluate the prototype on a larger and more varied dataset.
- No production deployment date has been agreed.

Write a manager-ready status update of no more than 100 words, using exactly these four headings:

Progress: State what the prototype currently does and report the initial test result, including the percentage of invoices processed correctly without manual correction.

Limitations: Explain the observed issues and identify what remains untested.

Next Step: State the planned next activity without presenting it as completed.

Deployment Status: Clarify whether a production deployment date has been agreed.

Rules:
- Distinguish observed test results from assumptions about future performance.
- Do not describe the prototype as production-ready.
- Do not invent metrics, deadlines, decisions, or capabilities.
- Do not omit any of the four requested sections.
- Output only the status update.

---

## Results After Prompt Revision

### GPT

> «Progress: The prototype extracts invoice numbers, dates, and totals from standard PDF invoices. In an initial test, 34 of 40 invoices (85%) were processed correctly without manual correction.  
> 
> Limitations: Six invoices required correction due to low-quality scans or unusual layouts. Handwritten invoices have not yet been tested.  
> 
> Next Step: Evaluate the prototype using a larger and more varied dataset to assess its performance across different invoice types.  
> 
> Deployment Status: No production deployment date has been agreed. The prototype has not been confirmed as production-ready.»

### Gemini

> «Progress  
> 
> The document-processing prototype extracts invoice numbers, dates, and totals from standard PDF invoices. In an initial test of 40 invoices, 34 (85%) were processed correctly without manual correction.  
> 
> Limitations  
> 
> Six invoices failed due to low-quality scans or unusual layouts. Handwritten invoices remain untested.  
> 
> Next Step  
> 
> The team plans to evaluate the prototype on a larger and more varied dataset.  
> 
> Deployment Status  
> 
> No production deployment date has been agreed upon.»

---

## Comparative Evaluation

| Criterion | Initial GPT | Initial Gemini | Revised GPT | Revised Gemini |
|---|---|---|---|---|
| Preserves key facts | Yes | Yes | Yes | Yes |
| Reports 85% success rate | Yes | No | Yes | Yes |
| Identifies observed limitations | Yes | Yes | Yes | Yes |
| Identifies untested handwritten invoices | Yes | Yes | Yes | Yes |
| Reports deployment status | Yes | Yes | Yes | Yes |
| Uses four prescribed headings | Not required | Not required | Yes | Yes |
| Respects the word limit | Yes | Yes | Yes | Yes |

### What Improved?

The revised prompt explicitly required a percentage, four named sections, a word limit, and a distinction between observed results and assumptions.

Both models followed the requested structure and included the 85% figure in the revised test.

The improvement was primarily in output consistency and compliance with the specified format, rather than a dramatic increase in factual accuracy.

### Remaining Limitations

Gemini described the six invoices as having "failed." The source notes only establish that they contained low-quality scans or unusual layouts and were not processed correctly without manual correction. The stronger wording may imply a more definitive failure than the notes support.

This illustrates why factual grounding requires attention not only to numbers and named entities, but also to the strength of the language used to describe results.

GPT added that the prototype had not been confirmed as production-ready. This is a cautious interpretation of the notes, not an independently measured readiness assessment.

---

## Key Learnings

1. **Source information must remain the factual boundary:** A model should not transform a limited test into a broad claim about system performance.
2. **Explicit structure improves consistency:** Named sections and required fields make outputs easier to review and compare.
3. **Quantitative details may need to be requested explicitly:** The initial GPT response included the percentage, while Gemini did not. Requiring the percentage led both models to report it in the revised test.
4. **Wording can change the meaning of evidence:** Terms such as "failed," "unreliable," and "production-ready" carry stronger implications than a description of the observed test results. A grounded response should preserve the level of certainty in its sources.
5. **A successful test is not proof of general reliability:** An 85% result on 40 invoices is a descriptive result from an initial sample. It does not establish performance on other datasets, handwritten invoices, or production workloads.

---

## Limitations

This experiment used one set of project notes, two prompt versions, and two models.

The results are exploratory. They do not establish that one model is generally more accurate or that the revised prompt will consistently outperform the initial prompt.

A more rigorous evaluation would use multiple project scenarios, predefined factual-accuracy criteria, and checks for omitted information, unsupported claims, and changes in certainty.

---

## Conclusion

This exercise demonstrates how AI can transform unstructured project notes into a manager-ready update while preserving the distinction between known facts, observed limitations, and planned work.

The central lesson is that grounded generation requires more than asking a model not to invent facts. It also benefits from explicit output requirements and careful evaluation of how the model interprets and communicates the evidence.

Prompt engineering is an iterative process: define the source of truth, specify the required structure, test the output, and check whether the wording remains faithful to the evidence.
