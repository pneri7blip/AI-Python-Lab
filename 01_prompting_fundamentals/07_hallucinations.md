# Reducing Hallucinations with Source-Grounded Prompts

## Objective
Explore how providing a defined source and explicitly restricting the model to that source can reduce unsupported or irrelevant information in AI responses.

## Prompt Used
> Answer the questions using ONLY the information explicitly provided in the source below.
>
> Do not use outside knowledge.
> Do not browse the web.
> Do not infer or invent missing information.
>
> If the answer is not explicitly stated in the source, write:
> "Not specified in the source."
>
> Source:
> EcoTrack Compliance Platform is an internal environmental compliance tool developed by GreenCore.
> Known information:
> Purpose: organize environmental compliance documents
> Main feature: document classification
> Supported file types: PDF and XLSX
> Pricing: not publicly available
> Integrations: not specified
> Release date: not specified
> Target users: environmental compliance teams

## Questions
1. What is the platform used for?
2. What is its main feature?
3. What file types does it support?
4. How much does it cost?
5. What integrations does it support?
6. When was it released?
7. Who is it designed for?

## Model Output
```text
1. What is the platform used for?
   To organize environmental compliance documents.

2. What is its main feature?
   Document classification.

3. What file types does it support?
   PDF and XLSX.

4. How much does it cost?
   Not publicly available.

5. What integrations does it support?
   Not specified in the source.

6. When was it released?
   Not specified in the source.

7. Who is it designed for?
   Environmental compliance teams.
```
## Evaluation

Tested with two LLMs (**GPT-5.6 Luna** and **Gemini 3.1 Pro**) to evaluate prompt portability and consistency. Both models followed the source restriction and correctly identified information that was explicitly provided while returning "Not specified in the source" for missing information.

In the initial test without a provided source, both models recognized that the requested product could not be reliably verified. However, Gemini additionally provided information about other products with similar names, demonstrating how models may introduce related but potentially irrelevant information when the requested source is unavailable.

## Key Takeaway

Providing a defined source and explicitly restricting the model to that source can reduce unsupported or irrelevant information. A clear fallback instruction for missing information also helps the model distinguish between known facts and information that is not available.
