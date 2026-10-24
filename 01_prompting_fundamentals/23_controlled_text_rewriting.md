# Controlled Text Rewriting

## Objective

Evaluate how well an LLM can shorten a professional message while respecting a strict word limit and preserving essential facts, deadlines, relationships between events, and the requested action.

---

## Initial Prompt

You are a professional text editor. Rewrite the following message according to the specified constraints.

Requirements:

- Reduce the text to a maximum of 45 words.
- Preserve all factual details, including dates, quantities, names, and deadlines.
- Keep the original meaning, key concerns, and requested action.
- Remove repetition and unnecessary wording.
- Do not add new information, assumptions, promises, or requests.
- Use clear, natural, professional English.
- Output only the rewritten message.

Original message:

"Hi Alex, I'm writing to follow up on the equipment delivery that we discussed last week. The delivery was originally scheduled for October 28, and we were told that the shipment would include 12 monitors and 6 docking stations. We still haven't received confirmation that the equipment has been dispatched. Since our team needs the equipment before the new employees start on November 3, could you please confirm whether the shipment has been sent and, if it hasn't, let us know the expected delivery date?"

---

## Initial Outputs

### GPT

> Hi Alex, I’m following up on the equipment delivery discussed last week, scheduled for October 28, including 12 monitors and 6 docking stations. We haven’t received dispatch confirmation. As the equipment is needed before new employees start on November 3, could you confirm whether it has shipped or provide the expected delivery date?

### Gemini

> Hi Alex, following up on our October 28 shipment of 12 monitors and 6 docking stations. We lack dispatch confirmation. Since new employees start November 3, please confirm if it has been sent or provide the expected delivery date.

---

## Initial Evaluation

Both models preserved the equipment quantities, the relevant dates, the missing dispatch confirmation, and the request for an update.

However, the outputs revealed two issues:

- **Word limit:** GPT's response exceeded the 45-word limit, while Gemini's response stayed within it.
- **Date interpretation:** Gemini described the equipment as an "October 28 shipment," which could imply that October 28 was the shipment date rather than the scheduled delivery date.

The initial prompt stated the constraints but did not explicitly distinguish the delivery date from the dispatch date.

---

## Prompt Revision 1

You are a professional text editor. Rewrite the message in no more than 45 words.

Follow these rules in order of priority:

1. Preserve the exact meaning of dates and their relationships to events. October 28 is the scheduled delivery date, not the dispatch date.
2. Preserve the quantities: 12 monitors and 6 docking stations.
3. Preserve the November 3 start date for the new employees and the urgency this creates.
4. Keep the request to confirm dispatch or provide an expected delivery date.
5. Remove repetition and unnecessary wording, but do not change facts or imply that an event has already happened.
6. Use clear, natural, professional English.

Output only the rewritten message.

Original message:

"Hi Alex, I'm writing to follow up on the equipment delivery that we discussed last week. The delivery was originally scheduled for October 28, and we were told that the shipment would include 12 monitors and 6 docking stations. We still haven't received confirmation that the equipment has been dispatched. Since our team needs the equipment before the new employees start on November 3, could you please confirm whether the shipment has been sent and, if it hasn't, let us know the expected delivery date?"

---

## Revised Outputs

### GPT

> Hi Alex, I’m following up on the equipment delivery scheduled for October 28, comprising 12 monitors and 6 docking stations. With new employees starting November 3, could you urgently confirm whether the shipment has been dispatched or provide an expected delivery date?

### Gemini

> Hi Alex, regarding the 12 monitors and 6 docking stations scheduled for delivery on October 28, we lack dispatch confirmation. Since new employees start November 3 and we need them before then, please confirm if it was sent or provide the expected delivery date.

---

## Evaluation After Revision

Both revised outputs stayed within the 45-word limit and correctly represented October 28 as the scheduled delivery date.

They also preserved the two equipment quantities, the November 3 start date, the missing dispatch confirmation, and the request for either dispatch confirmation or an expected delivery date.

The outputs differed slightly in emphasis:

- **GPT** produced a more concise message and communicated urgency directly.
- **Gemini** explicitly stated that the equipment was needed before the new employees started, making the reason for the deadline clearer.

Both models omitted the reference to the discussion held the previous week. This detail was not essential to the core request and could reasonably be removed to satisfy the word limit.

---

## Key Takeaway

Controlled text rewriting requires more than shortening a message. A useful prompt must establish which details are essential, define how dates and events relate to one another, and prioritize constraints when not every original detail can fit within a strict word limit.

In this test, explicitly clarifying the meaning of the delivery date helped both models produce outputs that better preserved the original intent.

The results demonstrate improved performance on this particular example, not a general guarantee of reliability. The evaluation covered one message and two models.
