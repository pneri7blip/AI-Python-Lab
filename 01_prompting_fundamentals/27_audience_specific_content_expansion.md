# Audience-Specific Content Expansion

## Objective

Explore how an AI model can adapt technical information for a non-technical audience while preserving factual accuracy and communicating uncertainty appropriately.

The exercise focuses on:

- Translating technical findings into accessible language.
- Explaining what test results mean without overstating their significance.
- Preserving important limitations and next steps.
- Adapting the level of explanation to the intended audience.

---

## Initial Prompt

You are a technical communication assistant.

Rewrite the following technical update for a non-technical business audience.

Technical update:
"Our document-processing prototype correctly extracted invoice numbers, dates, and totals from 34 out of 40 standard PDF invoices without manual correction. The remaining 6 invoices contained low-quality scans or unusual layouts. Handwritten invoices have not been tested. The next step is to evaluate the prototype on a larger and more varied dataset."

Write a clear, accessible explanation that helps a business manager understand what the results mean and what still needs to be tested.

Keep the explanation concise. Avoid unnecessary technical jargon. Do not invent facts or imply that the prototype is ready for production.

The prompt was tested with GPT and Gemini.

---

## Initial Results

### GPT

> «The prototype successfully extracted invoice numbers, dates, and totals from 34 of 40 standard PDF invoices without manual corrections. The remaining 6 invoices could not be processed correctly because they had poor scan quality or unusual layouts.  
> 
> These early results are promising, but further testing is needed. Handwritten invoices have not yet been tested, and the prototype still needs to be evaluated on a larger and more diverse set of invoices to better understand how reliably it performs in different situations. It is not yet ready for production use.»

### Gemini

> «Here is a summary of the document-processing prototype test:  
> 
> - **Current Results:** The tool successfully and automatically extracted key details (invoice numbers, dates, and totals) from 34 out of 40 standard PDF invoices. The 6 that failed involved low-quality scans or unusual layouts.  
> - **What Remains Untested:** We have not yet tested the prototype on handwritten invoices.  
> - **Next Steps:** We will evaluate the prototype using a larger and more diverse dataset to better understand its capabilities.»

---

## Initial Evaluation

Both models communicated the main results and identified the need for further testing.

- **GPT** explained the significance of the initial result and explicitly stated that the prototype was not ready for production.
- **Gemini** used a structured summary that was easy to scan, but it did not explicitly address production readiness.

Both models described the remaining invoices as failures, although the source notes only established that these invoices had low-quality scans or unusual layouts and were not processed correctly without manual correction.

This highlighted an important distinction: simplifying technical information should not make the description of the evidence more definitive than the source supports.

---

## Revised Prompt

You are a technical communication assistant writing for a non-technical business manager.

Rewrite the technical update below as a concise, plain-language explanation of what the results mean for the business.

Technical update:
"Our document-processing prototype correctly extracted invoice numbers, dates, and totals from 34 out of 40 standard PDF invoices without manual correction. The remaining 6 invoices contained low-quality scans or unusual layouts. Handwritten invoices have not been tested. The next step is to evaluate the prototype on a larger and more varied dataset. No production deployment date has been agreed."

Requirements:
- Explain the initial result in everyday language, including the fact that 34 of 40 invoices were processed correctly without manual correction.
- Explain what the test suggests and what it does not yet establish.
- Identify the main limitations and the planned next step.
- Make clear that production readiness has not been established.
- Avoid technical jargon, unsupported business benefits, and claims that the prototype is generally reliable.
- Do not describe the remaining invoices as complete failures unless the source explicitly establishes that.
- Use no more than 100 words.
- Output only the rewritten explanation.

---

## Results After Prompt Revision

### GPT

> «The prototype correctly captured invoice numbers, dates, and totals from 34 of 40 standard PDF invoices without manual correction. This is an encouraging initial result, but it does not yet show how well the prototype will perform across a wider range of invoices. Six invoices needed further attention due to poor scan quality or unusual layouts, and handwritten invoices have not been tested. The next step is to test a larger, more varied set of invoices. Production readiness has not been established, and no deployment date has been agreed.»

### Gemini

> «The prototype correctly extracted invoice numbers, dates, and totals from 34 out of 40 standard PDF invoices without manual correction. The remaining 6 invoices involved low-quality scans or unusual layouts, and handwritten invoices have not been tested. This test does not establish production readiness, and no deployment date has been agreed. The next step is to evaluate the prototype on a larger and more varied dataset.»

---

## Comparative Evaluation

| Criterion | Initial GPT | Initial Gemini | Revised GPT | Revised Gemini |
|---|---|---|---|---|
| Communicates the test result | Yes | Yes | Yes | Yes |
| Uses accessible language | Yes | Yes | Yes | Yes |
| Identifies untested handwritten invoices | Yes | Yes | Yes | Yes |
| Avoids overstating production readiness | Yes | Not explicit | Yes | Yes |
| Avoids categorical failure claims | No | No | Yes | Yes |
| Explains the limits of the evidence | Yes | Partially | Yes | Yes |

### What Improved?

The revised prompt made the expected interpretation more explicit. It required the models to distinguish an initial test result from broader conclusions about performance and to state that production readiness had not been established.

Both models followed these requirements in the second test.

- **GPT** provided a more interpretive explanation, describing the result as encouraging while emphasizing that broader performance remains unknown.
- **Gemini** remained more concise and factual, covering the results, limitations, and deployment status without adding a qualitative judgment.

The main improvement was greater consistency with the intended communication goals, rather than a dramatic change in overall response quality.

---

## Key Learnings

1. **Audience adaptation is more than simplifying vocabulary:** A business audience needs to understand not only what happened, but also what the result means and what remains uncertain.
2. **Preserve the strength of the evidence:** A model should not turn a limited test into a general claim about reliability. The wording must remain proportional to what was actually observed.
3. **State the intended interpretation explicitly:** Instructions to explain what results mean, identify what remains unknown, and avoid implying production readiness help establish clearer boundaries for the response.
4. **Different writing styles can both be valid:** GPT produced a more interpretive explanation, while Gemini favored a direct summary. The best choice depends on whether the audience needs more context or a concise factual update.
5. **Test against explicit criteria:** A useful evaluation checks not only readability, but also factual accuracy, uncertainty, completeness, and adherence to constraints.

---

## Limitations

This experiment used one technical update, two prompt versions, and two models.

The findings are exploratory and do not establish that the revised prompt will improve every audience-adaptation task.

A broader evaluation would test different audiences, levels of technical complexity, and source documents, using predefined criteria for accuracy, readability, and preservation of uncertainty.

---

## Conclusion

This exercise demonstrates how prompt engineering can help adapt technical information for a business audience without sacrificing factual precision.

The central lesson is that effective audience-specific generation requires the model to change how information is explained, not what the evidence supports.

A reliable workflow identifies the audience, defines the intended interpretation, specifies factual boundaries, and evaluates the resulting explanation against explicit criteria.
