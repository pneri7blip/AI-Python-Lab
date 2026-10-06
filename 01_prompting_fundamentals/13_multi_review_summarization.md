# Multi-Review Summarization

## Objective

Analyze multiple customer reviews and produce a concise summary that distinguishes recurring trends from isolated feedback.

The goal is to aggregate information across several reviews without treating a single customer's comment as a general trend.

---

## Initial Prompt

You are assisting a product operations analyst.

Analyze the customer reviews below and produce a concise summary of the main customer feedback.

Focus on:
- recurring positive points
- recurring negative points
- issues mentioned by multiple customers
- isolated issues that may still require attention

Do not treat a point mentioned by only one customer as a recurring trend.

Do not add information that is not explicitly stated in the reviews.

Keep the summary under 100 words.

Customer Reviews — Nova Wireless Headphones

Review 1:
The sound quality is excellent and the headphones are comfortable even after several hours of use. However, the carrying case feels too small.

Review 2:
I really like the sound quality and battery life. The headphones are comfortable, but the buttons are difficult to use while wearing gloves.

Review 3:
The battery lasts a long time and the sound is very clear. My only problem is that the carrying case is difficult to close.

Review 4:
Comfortable headphones with very good sound. The setup was easy, although the carrying case could be better designed.

Review 5:
The sound quality is impressive and the battery lasts well. I found the physical buttons slightly difficult to operate.

---

## Initial Outputs

### GPT-5.6 Luna

> **Recurring positives**
> - Excellent/very good sound quality (5/5 reviews).
> - Comfortable to wear (3/5).
> - Long battery life (3/5).
>
> **Recurring negatives**
> - Carrying case has design/usability issues (3/5).
> - Physical buttons are difficult to operate (2/5).
>
> **Issues requiring attention**
> - Case is too small, difficult to close, and could be better designed.
> - Buttons may be particularly difficult to use while wearing gloves.
>
> **Isolated**
> - One customer mentioned setup was easy.

### Gemini 3.1 Pro

> **Recurring Positives**
> - Sound Quality: Universally praised across all five reviews.
> - Comfort & Battery: Consistently noted as comfortable for extended use (3 reviews) and having a long battery life (3 reviews).
>
> **Recurring Negatives**
> - Carrying Case: Cited as poorly designed, too small, or difficult to close (3 reviews).
> - Button Usability: Physical buttons are difficult to operate (2 reviews).
>
> **Isolated Points**
> - Glove Compatibility: Buttons are specifically hard to press while wearing gloves (1 review).
> - Setup: Easy setup process was mentioned (1 review).

---

## Issue Identified

Both models correctly identified the main recurring positive and negative themes.

However, GPT-5.6 Luna placed the specific difficulty of using the buttons while wearing gloves under "Issues requiring attention" rather than clearly classifying it as an isolated finding.

While the initial prompt attempted to separate recurring trends from isolated feedback, the classification rule lacked an explicit numerical threshold to guarantee consistent separation across different models.

---

## Prompt Revision 1

The following quantitative classification rules were added to remove ambiguity:

Classify each finding according to how often it appears:
- Recurring: mentioned by at least two customers.
- Isolated: mentioned by only one customer.

Keep recurring findings separate from isolated findings.
Do not present an isolated finding as a recurring trend.
Do not add information that is not explicitly stated in the reviews.

---

## Revised Outputs

### GPT-5.6 Luna

> **Recurring**
> - **Positive:** Excellent/very good sound quality (5/5); comfortable to wear (3/5); long-lasting battery (3/5).
> - **Negative:** Carrying case has design/usability problems (3/5); physical buttons are difficult to operate (2/5).
>
> **Isolated**
> - Buttons are difficult to use while wearing gloves (Review 2).
> - Setup was easy (Review 4).
>
> All findings are based only on the reviews provided.

### Gemini 3.1 Pro

> **Recurring Findings**
> - Positive: High sound quality, long battery life, and comfortable fit.
> - Negative: The carrying case is poorly designed (undersized and difficult to close), and the physical buttons are hard to operate.
>
> **Isolated Findings**
> - Positive: The setup process is easy.

---

## Evaluation

Tested with two LLMs (GPT-5.6 Luna and Gemini 3.1 Pro) across two prompt iterations to evaluate multi-review summarization, trend classification, and information retention.

In the initial test, both models correctly identified the main recurring themes. However, GPT-5.6 Luna grouped the specific difficulty of using the buttons while wearing gloves under "issues requiring attention" rather than clearly isolating it.

The first prompt revision introduced explicit frequency-based threshold rules (`>= 2` vs `= 1`). Following this revision, GPT-5.6 Luna correctly categorized the glove-related issue as isolated.

Gemini 3.1 Pro also maintained the recurring/isolated structure, but opted to omit the glove-related detail entirely from its isolated section to favor brevity. This demonstrates that while explicit classification rules improve categorization accuracy, models may still vary in their information retention strategies for low-frequency data.

---

## Key Takeaway

Multi-review summarization requires more than identifying common themes: it demands strict criteria to distinguish broad trends from edge-case user feedback.

In this experiment, setting explicit numerical thresholds (`>= 2` vs `= 1`) prevented models from elevating individual complaints into general product issues. Additionally, the comparison revealed that under strict compression, different LLMs may handle isolated data differently—either listing it explicitly or filtering it out as noise.
