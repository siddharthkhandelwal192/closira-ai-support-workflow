# Prompt Design

## Objective

The goal of the prompt design was to create a customer support assistant that:
- answers only from SOP data
- avoids hallucinations
- escalates sensitive or unknown queries
- keeps responses short and human-like

---

# System Prompt Strategy

The assistant is instructed to:

- use only SOP information
- avoid inventing details
- escalate when information is missing
- keep replies concise and professional

The prompt explicitly mentions:
- Botox pricing exists in SOP
- Fillers pricing exists in SOP
- consultation details exist in SOP

This was added because smaller/free LLMs sometimes hallucinate extra pricing information.

---

# Hallucination Prevention

To reduce hallucinations:
- the assistant is repeatedly instructed not to invent details
- escalation behavior is preferred over guessing
- responses are intentionally kept short

Example:

Correct:
"Botox starts from £200."

Incorrect:
"Forehead Botox costs £5000."

---

# Confidence-Based Escalation

The workflow escalates when:
- complaint keywords appear
- refund requests appear
- medical queries appear
- information is unavailable

Escalation reasons are also logged in:
`escalation_log.txt`

The project uses simple keyword-based escalation instead of advanced confidence scoring models.

---

# Tone and Persona

The assistant was designed to behave like a professional SMB customer support representative.

Tone characteristics:
- short
- polite
- human-like
- professional
- conversational

---

# Why Simple Architecture Was Chosen

The project intentionally avoids:
- vector databases
- RAG pipelines
- frontend frameworks
- complex agent systems

The focus was instead placed on:
- workflow clarity
- prompt quality
- conversational logic
- safe response behavior

which were more relevant for the assignment scope.