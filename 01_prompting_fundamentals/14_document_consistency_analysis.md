# Inconsistency Detection

## Objective

Identify contradictions and inconsistencies within an operational report without assuming which statement is correct.

The goal is to detect conflicting information, group related conflicts together, and explain the inconsistency using only information explicitly stated in the source.

---

## Initial Prompt

You are assisting an operations analyst.

Review the information below and identify any contradictions or inconsistencies.

For each inconsistency, provide:
- Issue
- Conflicting Information
- Explanation

Use only information explicitly stated in the source.
Do not assume which statement is correct.

If no contradiction is found, write: "No contradiction identified."

Operations Report — Northbridge Distribution Center

The report states that the facility operates 24 hours a day, seven days a week.

The staffing section states that the facility operates with three shifts:
- Morning shift: 06:00–14:00
- Afternoon shift: 14:00–22:00
- Night shift: 22:00–06:00

The report states that all three shifts operate every day of the week.

The maintenance section states that the facility is closed every Sunday for scheduled maintenance.

The report also states that deliveries are received seven days a week, including Sundays.

The current warehouse capacity is reported as 8,000 units.

A later section of the report states that the warehouse has capacity for 10,000 units.

---

## Initial Outputs

### GPT-5.6 Luna

> **Issue 1: Facility operating schedule**
> - **Conflicting Information:** The facility operates 24 hours a day, seven days a week. / The facility is closed every Sunday for scheduled maintenance.
> - **Explanation:** These statements conflict because one states continuous operation seven days a week, while the other states the facility is closed every Sunday.
>
> **Issue 2: Sunday operations**
> - **Conflicting Information:** All three shifts operate every day of the week. / The facility is closed every Sunday.
> - **Explanation:** The report states that all shifts operate on Sundays, but also states that the facility is closed every Sunday.
>
> **Issue 3: Sunday deliveries**
> - **Conflicting Information:** Deliveries are received seven days a week, including Sundays. / The facility is closed every Sunday.
> - **Explanation:** The report states that deliveries are received on Sundays while also stating that the facility is closed every Sunday.
>
> **Issue 4: Warehouse capacity**
> - **Conflicting Information:** Current warehouse capacity is 8,000 units. / The warehouse has capacity for 10,000 units.
> - **Explanation:** Two different capacity figures are given for the warehouse. The report does not indicate which figure is correct.

### Gemini 3.1 Pro

> **Issue: Facility Operating Schedule**
> - **Conflicting Information:** The report states the facility operates 24 hours a day, seven days a week, and that all three shifts operate every day of the week. However, the maintenance section states the facility is closed every Sunday for scheduled maintenance.
> - **Explanation:** The facility cannot operate continuously every day of the week if it undergoes a full closure every Sunday.
>
> **Issue: Sunday Deliveries**
> - **Conflicting Information:** The report states that deliveries are received seven days a week, explicitly including Sundays. However, it also states the facility is closed every Sunday.
> - **Explanation:** The facility cannot receive deliveries on Sundays if it is entirely closed for maintenance on that day.
>
> **Issue: Warehouse Capacity**
> - **Conflicting Information:** One section reports the current warehouse capacity as 8,000 units, while a later section states the capacity is 10,000 units.
> - **Explanation:** The report provides two different, mutually exclusive figures for the maximum unit capacity of the warehouse.

---

## Issue Identified

Both models identified the main contradictions in the report. However, they differed in how they grouped related statements.

GPT-5.6 Luna treated the facility's operating schedule, Sunday operations, and Sunday deliveries as three separate inconsistencies, while Gemini 3.1 Pro grouped the operating schedule and Sunday operations together but kept Sunday deliveries as a separate issue.

The underlying problem was that the prompt lacked explicit instructions on how to group multiple manifestations of the same core conflict.

---

## Prompt Revision 1

The following consolidation rules were added to the prompt:

Group related statements into a single inconsistency when they describe the same underlying conflict.
Do not treat multiple manifestations of the same conflict as separate inconsistencies.

---

## Revised Outputs

### GPT-5.6 Luna

> **Inconsistency 1 — Facility operating status and Sunday operations**
> - **Issue:** The report gives conflicting information about whether the facility operates on Sundays.
> - **Conflicting Information:**
>   - The facility operates 24 hours a day, seven days a week.
>   - All three shifts operate every day of the week.
>   - The facility is closed every Sunday for scheduled maintenance.
>   - Deliveries are received seven days a week, including Sundays.
> - **Explanation:** The statements that the facility operates continuously and that all shifts operate every day conflict with the statement that the facility is closed every Sunday. The statement about Sunday deliveries also conflicts with the facility being closed every Sunday.
>
> **Inconsistency 2 — Warehouse capacity**
> - **Issue:** The report gives two different figures for warehouse capacity.
> - **Conflicting Information:**
>   - Current warehouse capacity: 8,000 units.
>   - Warehouse capacity: 10,000 units.
> - **Explanation:** The report states two different capacity figures without explaining a change or distinction between them.

### Gemini 3.1 Pro

> **Issue: Facility Operating Schedule vs. Sunday Maintenance Closure**
> - **Conflicting Information:** The report states the facility operates 24 hours a day, seven days a week, with all shifts working every day and deliveries received on Sundays. Conversely, the maintenance section states the facility is closed every Sunday for scheduled maintenance.
> - **Explanation:** The facility cannot be fully operational, running shifts, and receiving deliveries on Sundays if it is simultaneously closed for maintenance every Sunday.
>
> **Issue: Warehouse Capacity Discrepancy**
> - **Conflicting Information:** The current warehouse capacity is reported as 8,000 units, but a later section states the warehouse has a capacity for 10,000 units.
> - **Explanation:** The document provides two different, mutually exclusive numbers for the total unit capacity of the same facility.

---

## Evaluation

Tested with two LLMs (GPT-5.6 Luna and Gemini 3.1 Pro) across two prompt iterations to evaluate inconsistency detection, conflict grouping, and source fidelity.

In the initial test, both models identified the main contradictions, but they grouped related statements differently. GPT-5.6 Luna reported four separate inconsistencies, while Gemini 3.1 Pro reported three.

The prompt was then revised to explicitly require related statements describing the same underlying conflict to be grouped together.

After the revision, both models aligned on two primary inconsistencies: the macro-conflict surrounding Sunday operations/deliveries versus the Sunday maintenance closure, and the warehouse capacity discrepancy.

The results demonstrate that explicit grouping rules successfully eliminate artificially inflated issue lists in automated report analysis.

---

## Key Takeaway

Inconsistency detection is not only about identifying conflicting statements: it requires clear instructions on how related conflicts should be aggregated without introducing unsupported assumptions.

In this experiment, adding explicit grouping criteria reduced fragmentation across LLM outputs, producing a consolidated, root-cause-oriented analysis of operational discrepancies.
