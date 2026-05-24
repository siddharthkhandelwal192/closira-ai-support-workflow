# Closira AI Engineering Internship Assignment

## AI Customer Support Workflow

This project is a simple AI-powered customer support workflow built for the Closira AI Engineering Internship assignment.

The workflow simulates how SMB businesses can use AI for first-level customer support while keeping responses grounded in SOP information.

---

# Features

- FAQ answering using SOP data
- Lead qualification workflow
- Escalation detection
- Hallucination prevention
- Structured conversation summary generation

---

# Tech Stack

- Python
- OpenRouter API
- OpenAI SDK
- Prompt Engineering

---

# Project Structure

closira_assignment/

├── app.py  
├── sop.txt  
├── README.md  
├── prompt_design.md  
├── requirements.txt  
├── escalation_log.txt  

├── screenshots/  
│ ├── faq.png  
│ ├── escalation.png  
│ └── summary.png  

└── test_transcripts/  
├── faq_test.md  
├── escalation_test.md  
├── out_of_scope_test.md  
├── qualification_test.md  
└── summary_test.md  

---

# Setup Instructions

Install dependencies:

```bash
pip install openai
```

Run the project:

```bash
python3.11 app.py
```

---

# API Key Setup

Before running the project, add your OpenRouter API key inside `app.py`:

```python
api_key="YOUR_OPENROUTER_API_KEY"
```

Free API keys can be generated from:
https://openrouter.ai/

---

# SOP Grounding

The assistant is instructed to answer ONLY from the provided SOP information.

If information is unavailable:
- the assistant escalates to a human agent
- avoids hallucinating information
- avoids inventing pricing or policies

---

# Escalation Logic

Escalation happens when:
- complaint keywords are detected
- refund/angry sentiment appears
- medical queries are asked
- information is unavailable in SOP

Escalation reasons are logged in:
`escalation_log.txt`

---

# Design Decisions

This project was intentionally designed as a lightweight CLI workflow instead of a complex production system.

Main focus areas:
- SOP-grounded responses
- hallucination prevention
- escalation handling
- conversational workflow clarity
- simple and understandable architecture

---

# Trade-offs and Limitations

- The project uses a simple keyword-based escalation system instead of advanced sentiment analysis.
- SOP retrieval is prompt-based and does not use vector databases or RAG pipelines.
- The workflow is CLI-based and does not include a frontend UI.
- Smaller/free LLMs may occasionally require stronger prompt constraints.
- The implementation prioritizes simplicity and workflow clarity over production-scale architecture.

---

# Video Walkthrough

The walkthrough video demonstrates:
- FAQ handling
- escalation flow
- lead qualification
- summary generation