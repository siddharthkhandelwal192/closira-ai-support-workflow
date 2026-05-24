from openai import OpenAI

# OpenRouter client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="YOUR_OPENROUTER_API_KEY"
)

# Load SOP data
with open("sop.txt", "r") as file:
    sop = file.read()

# Store conversation history
history = []

# Store lead qualification answers
lead_info = {}

# Lead qualification questions
questions = [
    "What type of business are you running?",
    "How big is your team?",
    "What tools are you currently using?"
]

# Main system prompt
system_prompt = f"""
You are a customer support assistant for Bloom Aesthetics Clinic.

You MUST answer ONLY using the exact information written in the SOP.

VERY IMPORTANT RULES:
- Do NOT invent pricing
- Do NOT invent treatment details
- Do NOT invent policies
- Do NOT add extra explanations
- If exact information is unavailable, say:
  "I’m not sure about that information. I’ll connect you with a human support agent."

Keep replies:
- short
- professional
- human-like

SOP:
{sop}
"""

print("\nAI SUPPORT ASSISTANT\n")

# Lead Qualification Stage
for q in questions:

    ans = input(q + "\n> ")

    lead_info[q] = ans

print("\nQualification complete.\n")

# Main Chat Loop
while True:

    user_input = input("Customer: ")

    # Exit condition
    if user_input.lower() == "exit":
        break

    # Escalation keywords
    escalation_words = [
        "complaint",
        "refund",
        "angry",
        "manager",
        "medical",
        "lawsuit",
        "terrible"
    ]

    escalation = False

    for word in escalation_words:

        if word in user_input.lower():

            escalation = True

    # Escalation response
    if escalation:

        reason = "Customer complaint or escalation keyword detected"

        print("\nAI: I’m escalating this conversation to a human support agent.\n")

        # Save escalation log
        with open("escalation_log.txt", "a") as log:

            log.write(f"Customer Message: {user_input}\n")
            log.write(f"Reason: {reason}\n\n")

        continue

    # Save user message
    history.append({
        "role": "user",
        "content": user_input
    })

    # Hardcoded FAQ handling for reliability
    if "botox" in user_input.lower():

        reply = "Botox starts from £200."

    elif "filler" in user_input.lower():

        reply = "Fillers start from £250."

    elif "consultation" in user_input.lower():

        reply = "Consultations are free."

    else:

        # Generate AI response
        try:

            response = client.chat.completions.create(
                model="openai/gpt-oss-20b:free",
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt
                    }
                ] + history,
                max_tokens=150
            )

            # Extract reply
            reply = response.choices[0].message.content

        except Exception:

            reply = "I’m not sure about that information. I’ll connect you with a human support agent."

    # Print AI reply
    print(f"\nAI: {reply}\n")

    # Save AI reply
    history.append({
        "role": "assistant",
        "content": reply
    })

# Summary Prompt
summary_prompt = f"""
Generate a short customer support summary.

Include:
- Customer intent
- Lead details
- Main questions asked
- SOP gaps identified
- Recommended next step

Lead Info:
{lead_info}

Conversation:
{history}
"""

# Generate summary
try:

    summary = client.chat.completions.create(
        model="openai/gpt-oss-20b:free",
        messages=[
            {
                "role": "system",
                "content": summary_prompt
            }
        ],
        max_tokens=200
    )

    final_summary = summary.choices[0].message.content

except Exception:

    final_summary = """
Customer Intent:
Asked about pricing and services.

Lead Details:
Collected during qualification stage.

Recommended Next Step:
Human follow-up recommended.
"""

print("\nFINAL SUMMARY:\n")

print(final_summary)