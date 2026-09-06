## Prompt Used
> Perform the following actions on the text delimited by triple backticks:
>
> 1. Summarize the customer's technical issue in 1 sentence.
> 2. Determine the urgency level (Low, Medium, or High) based on business impact.
> 3. Extract any device or operating system details mentioned.
> 4. Output a JSON object containing the keys: `issue_summary`, `urgency`, and `system_details`.
>
> Use the following format:
>
> Summary: <1 sentence summary>
> Urgency: <Low/Medium/High>
> System Details: <extracted details or "Not specified">
> JSON Output: <json object with issue_summary, urgency, and system_details>
>
> Ticket Text: ```<text>```
Input Text

Hello support, after updating my iPhone 15 Pro to iOS 18, the payment gateway in your app freezes every time I attempt to complete a transaction. I need to process client invoices today for payroll, so this is causing major business disruption. Please help ASAP!

Model Output

Summary: The customer's payment gateway freezes during transactions after updating their iPhone 15 Pro to iOS 18, causing a major business disruption.  
Urgency: High  
System Details: iPhone 15 Pro, iOS 18  
JSON Output: {  
  "issue_summary": "The customer's payment gateway freezes during transactions after updating their iPhone 15 Pro to iOS 18, causing a major business disruption.",  
  "urgency": "High",  
  "system_details": "iPhone 15 Pro, iOS 18"  
}

Evaluation

Tested across two LLMs (GPT-5.6 Luna and Gemini 3.1 Pro) to evaluate prompt portability. Both models followed the step-by-step instructions and returned valid JSON matching the requested schema.

Key Takeaway

Breaking the task into clear steps helps the model handle each part of the request without skipping important details. Defining the output structure also makes the result easier to read and process programmatically.

