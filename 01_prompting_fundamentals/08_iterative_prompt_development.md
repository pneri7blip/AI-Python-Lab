# Iterative Prompt Development

## Objective

Explore how a prompt can be progressively refined by identifying issues in the model's output and making targeted changes to the prompt.

The goal is to improve both output length and factual consistency while keeping the original task unchanged.

## Product Fact Sheet

PRODUCT: TerraDesk Standing Desk

OVERVIEW
- Height-adjustable electric standing desk
- Designed for home offices and professional workspaces
- Available in white, black, and oak finishes
- Dual-motor electric adjustment system

FEATURES
- Height range: 72–120 cm
- Memory function with 3 programmable height settings
- Maximum load: 100 kg
- Cable management tray included

MATERIALS
- Steel frame
- 25 mm laminated desktop

WARRANTY
- 5-year warranty

---

## Iteration 0: Initial Prompt

### Prompt

Your task is to help a marketing team create a product description for a retail website.

Write a product description based on the product fact sheet provided below.

Product fact sheet:

[Product fact sheet provided above.]

### Initial Output

#### GPT-5.6 Luna

> TerraDesk Standing Desk
>
> Create a more flexible and comfortable workspace with the TerraDesk Standing Desk, an electric height-adjustable desk designed for both home offices and professional environments.
>
> Its dual-motor electric adjustment system lets you easily switch between sitting and standing positions, with a height range from 72 to 120 cm. The built-in memory function allows you to save up to three preferred height settings for quick adjustments throughout your workday.
>
> Built for everyday use, the TerraDesk combines a sturdy steel frame with a 25 mm laminated desktop and supports loads of up to 100 kg. A practical cable management tray keeps your workspace organized and helps reduce cable clutter.
>
> Available in white, black, and oak finishes, the TerraDesk can complement a wide range of office styles.
>
> Key features:
> - Electric height adjustment from 72–120 cm
> - Dual-motor adjustment system
> - 3 programmable memory settings
> - Maximum load: 100 kg
> - Steel frame with 25 mm laminated desktop
> - Integrated cable management tray
> - Available in white, black, and oak
> - 5-year warranty

#### Gemini 3.1 Pro

> TerraDesk Standing Desk
>
> Transform the way you work with the TerraDesk Standing Desk, a premium electric height-adjustable desk designed to elevate both home offices and professional workspaces. Engineered with a powerful dual-motor system, the TerraDesk offers smooth and quiet transitions from sitting to standing, helping you stay active, comfortable, and focused throughout your workday.
>
> Key Features:
>
> - Versatile Height Range: Effortlessly glide between 72 cm and 120 cm to find your perfect ergonomic posture.
> - Smart Memory Presets: Save your ideal sitting and standing positions with 3 programmable memory settings for instant, one-touch adjustments.
> - Heavy-Duty Capacity: A robust build easily supports up to 100 kg.
> - Clutter-Free Organization: An integrated cable management tray keeps cords neatly tucked away.
>
> Premium Build & Design:
> Built for daily durability, the TerraDesk features a steel frame and a 25 mm laminated desktop. To match different workspace styles, the TerraDesk is available in white, black, and oak finishes.
>
> Warranty:
> The TerraDesk comes with a 5-year warranty.

### Issue 1: Output Too Long

The initial responses contain more detail than necessary for a short retail product description.

The task does not specify a maximum length, so the models produce relatively detailed marketing copy.

The first refinement should therefore address output length without changing the underlying task.

---

## Iteration 1: Limit the Output Length

### Prompt Revision

The original prompt is kept unchanged, with one additional instruction:

> Use at most 80 words.

### Revised Prompt

Your task is to help a marketing team create a product description for a retail website.

Write a product description based on the product fact sheet provided below.

Use at most 80 words.

Product fact sheet:

[Product fact sheet provided above.]

### Revised Output

#### GPT-5.6 Luna

> Transform your workspace with the TerraDesk Standing Desk, an electric height-adjustable desk designed for home and professional offices. Its dual-motor system adjusts smoothly from 72–120 cm, while three programmable memory settings make switching between preferred heights effortless. A sturdy steel frame and 25 mm laminated desktop support up to 100 kg. The included cable management tray keeps your workspace tidy. Available in white, black, and oak, with a 5-year warranty.

#### Gemini 3.1 Pro

> Upgrade your workspace with the TerraDesk Standing Desk, an electric dual-motor desk designed for both home and professional offices.
>
> Key Features:
> - Smooth Transitions: Effortlessly adjust from 72–120 cm using the smart keypad with 3 programmable memory settings.
> - Heavy-Duty Build: A robust steel frame and 25 mm laminated desktop easily support up to 100 kg.
> - Clutter-Free Setup: Keeps cords hidden with the included cable management tray.
>
> Available in white, black, or oak finishes, and backed by a 5-year warranty.

### Issue 2: Unsupported Claims

The 80-word constraint successfully controls the length of the output, but a second issue becomes visible.

Some statements are not explicitly supported by the product fact sheet.

For example, Gemini describes a "smart keypad", but the fact sheet only specifies a memory function with three programmable height settings.

Gemini also describes "Smooth Transitions" and GPT-5.6 Luna says the system "adjusts smoothly".

Neither the smooth adjustment nor the keypad is explicitly stated in the source.

This shows that controlling output length alone does not prevent the model from adding unsupported product claims.

---

## Iteration 2: Ground the Output in the Source

### Prompt Revision

The previous 80-word constraint is retained, and two additional instructions are added:

> Use only information explicitly stated in the product fact sheet.
> Do not add features, specifications, benefits, or claims that are not supported by the fact sheet.

### Final Prompt

Your task is to help a marketing team create a product description for a retail website.

Write a product description based on the product fact sheet provided below.

Use at most 80 words.

Use only information explicitly stated in the product fact sheet.
Do not add features, specifications, benefits, or claims that are not supported by the fact sheet.

Product fact sheet:

PRODUCT: TerraDesk Standing Desk

OVERVIEW
- Height-adjustable electric standing desk
- Designed for home offices and professional workspaces
- Available in white, black, and oak finishes
- Dual-motor electric adjustment system

FEATURES
- Height range: 72–120 cm
- Memory function with 3 programmable height settings
- Maximum load: 100 kg
- Cable management tray included

MATERIALS
- Steel frame
- 25 mm laminated desktop

WARRANTY
- 5-year warranty

### Final Output

#### GPT-5.6 Luna

> Meet the TerraDesk Standing Desk, a height-adjustable electric desk designed for home offices and professional workspaces. Its dual-motor electric adjustment system offers a height range of 72–120 cm, with a memory function featuring three programmable height settings. The steel frame and 25 mm laminated desktop support up to 100 kg. Available in white, black, and oak finishes, it includes a cable management tray and comes with a 5-year warranty.

#### Gemini 3.1 Pro

> The TerraDesk Standing Desk is an electric height-adjustable desk designed for home offices and professional workspaces. Built with a steel frame and a 25 mm laminated desktop, its dual-motor system adjusts from 72 to 120 cm. It supports a maximum load of 100 kg and features a memory function with 3 programmable height settings. Available in white, black, and oak finishes, it includes a cable management tray and is backed by a 5-year warranty.

---

## Evaluation

Tested with two LLMs (GPT-5.6 Luna and Gemini 3.1 Pro) across multiple prompt iterations.

The initial prompts produced detailed marketing copy and included some claims that were not explicitly supported by the product fact sheet.

Adding an 80-word limit successfully controlled the output length, but did not by itself prevent unsupported claims.

The final iteration added explicit source-grounding instructions. Both models then produced concise descriptions using information supported by the provided fact sheet.

The experiment demonstrates how targeted prompt revisions can address different issues independently.

## Key Takeaway

Iterative prompt development involves analyzing the model's output, identifying specific problems, and making targeted changes to the prompt.

In this experiment, an output-length constraint addressed verbosity, while explicit source-grounding instructions helped prevent unsupported product claims. This approach can make prompts more precise, controllable, and reliable.
