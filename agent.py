from google.adk.agents import Agent

# -------------------------
# TOOL / ACTION FUNCTION
# -------------------------
def square_number(n: int) -> int:
    return n * n


# -------------------------
# AUTONOMOUS AGENT
# -------------------------
root_agent = Agent(
    name="autonomous_agent",
    model="groq/llama-3.1-8b-instant",
    instruction=(
        "You are an autonomous agent.\n"
        "You receive a goal and repeatedly follow this loop:\n"
        "1. Think about the next step\n"
        "2. Act to achieve the goal\n"
        "3. Evaluate if the goal is achieved\n"
        "Stop once the goal is completed.\n\n"
        "Goal: Find the square of 5.\n"
        "When the result is obtained, confirm success and stop."
    ),
    tools=[square_number]
)
