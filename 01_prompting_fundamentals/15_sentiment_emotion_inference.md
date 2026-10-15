# Sentiment & Emotion Inference

## Objective

Evaluate how prompt instructions affect sentiment classification, emotion inference, and the extraction of positive and negative aspects from a customer review.

The exercise compares two model outputs before and after refining the prompt.

## Initial Prompt

You are assisting a customer experience analyst.

Analyze the following customer review.

Return a JSON object with these fields:
- "Sentiment": "positive", "negative", or "neutral"
- "Emotions": a list of up to three emotions explicitly supported by the review
- "Positive_Aspects": a list of positive points mentioned
- "Negative_Aspects": a list of negative points mentioned

Use only information supported by the review.
Do not infer emotions, intentions, or circumstances that are not supported by the text.
If a list has no supported items, return an empty list.
Return valid JSON only.

Customer Review:

"The laptop performs well and the screen is excellent. However, the battery barely lasts four hours, which is disappointing for a device in this price range. Customer support replaced the charger quickly when it failed, and I appreciated how efficiently they handled that issue. Overall, I like the laptop, but I expected better battery life."

## Initial Outputs

### GPT-5.6 Luna

{
  "Sentiment": "positive",
  "Emotions": [
    "Disappointment",
    "Appreciation"
  ],
  "Positive_Aspects": [
    "Laptop performs well",
    "Screen is excellent",
    "Customer support replaced the failed charger quickly",
    "Customer support handled the issue efficiently",
    "Customer likes the laptop overall"
  ],
  "Negative_Aspects": [
    "Battery barely lasts four hours",
    "Battery life is below expectations for a device in this price range"
  ]
}

### Gemini 3.1 Pro

{
  "Sentiment": "neutral",
  "Emotions": [
    "disappointing"
  ],
  "Positive_Aspects": [
    "The laptop performs well",
    "The screen is excellent",
    "Customer support replaced the charger quickly when it failed",
    "Customer support handled the charger issue efficiently",
    "Overall, I like the laptop"
  ],
  "Negative_Aspects": [
    "The battery barely lasts four hours",
    "Battery life is disappointing for a device in this price range",
    "The charger failed",
    "Expected better battery life"
  ]
}

## Issue Identified

The initial outputs showed several differences:

- Sentiment ambiguity: GPT classified the review as positive, while Gemini classified it as neutral. The prompt did not explain how to weigh mixed opinions or interpret an explicit overall judgment.
- Inconsistent emotion labels: GPT used emotion nouns, while Gemini returned "disappointing", an adjective that describes an evaluation rather than clearly naming an emotion.
- Redundant aspects: Some statements described the same underlying issue, particularly the short battery life and the customer's disappointment with it.
- Different treatment of the charger failure: The charger failure was a negative event, but customer support resolved it quickly and efficiently. The prompt did not explicitly distinguish the event from its resolution.

## Prompt Revision 1

The revised prompt introduced clearer classification criteria, required lowercase emotion nouns, and instructed the models to combine repeated statements about the same issue.

You are assisting a customer experience analyst.

Analyze the following customer review.

Return a JSON object with these fields:
- "Sentiment": "positive", "negative", or "neutral"
- "Emotions": a list of up to three emotions explicitly supported by the review, expressed as lowercase nouns
- "Positive_Aspects": a list of positive points mentioned
- "Negative_Aspects": a list of negative points mentioned

Apply these rules:
- Determine sentiment from the review as a whole. Give appropriate weight to explicit overall judgments, while considering both positive and negative evidence.
- Use "neutral" when the review contains mixed opinions without a clearly dominant overall sentiment.
- Include only emotions supported by explicit wording or clear textual evidence. Use emotion nouns, not adjectives or descriptions of situations.
- List each distinct aspect only once. Combine repeated statements about the same underlying issue.
- Distinguish a negative event from the way it was resolved. Do not describe a successfully resolved issue as an ongoing service failure.
- Use only information supported by the review.
- If a list has no supported items, return an empty list.

Return valid JSON only.

Customer Review:

"The laptop performs well and the screen is excellent. However, the battery barely lasts four hours, which is disappointing for a device in this price range. Customer support replaced the charger quickly when it failed, and I appreciated how efficiently they handled that issue. Overall, I like the laptop, but I expected better battery life."

## Revised Outputs

### GPT-5.6 Luna

{
  "Sentiment": "positive",
  "Emotions": [
    "disappointment",
    "appreciation"
  ],
  "Positive_Aspects": [
    "Laptop performs well",
    "Screen is excellent",
    "Customer support replaced the failed charger quickly and efficiently",
    "Customer likes the laptop overall"
  ],
  "Negative_Aspects": [
    "Battery life is short, lasting barely four hours and falling short of expectations for a device in this price range"
  ]
}

### Gemini 3.1 Pro

{
  "Sentiment": "positive",
  "Emotions": [
    "disappointment"
  ],
  "Positive_Aspects": [
    "Good performance",
    "Excellent screen",
    "Quick and efficient customer support resolution when charger failed"
  ],
  "Negative_Aspects": [
    "Short battery life (barely lasts four hours)"
  ]
}

## Evaluation

The revised prompt improved agreement between the two models on the overall sentiment: both classified the review as positive.

The revised outputs were also more concise. Both models combined the battery-related criticism into a single aspect, and neither treated the resolved charger failure as a separate ongoing service problem.

However, some differences remained:

- Emotion coverage: GPT identified both disappointment and appreciation, while Gemini identified only disappointment. The prompt permits up to three emotions but does not require every explicitly supported emotion to be included.
- Aspect coverage: GPT explicitly mentioned that the customer liked the laptop overall. Gemini omitted this point from its positive aspects, although it classified the overall sentiment as positive.
- Sentiment interpretation: Agreement improved, but this does not independently establish that the classification is correct. The review contains mixed evidence, and the explicit overall judgment is an important factor in interpreting it.

The comparison suggests that more precise instructions can improve consistency and reduce redundant output, but they do not guarantee identical results or complete extraction.

## Key Takeaway

Effective prompt engineering requires more than specifying an output format. Clear classification criteria, consistent label conventions, and instructions for handling overlapping information can improve model outputs.

Comparing models before and after a prompt revision also helps reveal residual differences in interpretation and information coverage. Agreement should be evaluated alongside evidence fidelity and completeness, rather than treated as proof of correctness.
