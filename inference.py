import os
from openai import OpenAI
from tasks import get_tasks

# ✅ MUST use LiteLLM proxy (important for validation)
client = OpenAI(
    base_url=os.environ["API_BASE_URL"],
    api_key=os.environ["API_KEY"]
)

def choose_action(tasks):
    prompt = f"""
You are a task scheduling AI.

Tasks:
{tasks}

Choose the best task index (0-based) based on highest priority.
Return ONLY the index number.
"""

    response = client.chat.completions.create(
        model=os.environ.get("MODEL_NAME", "gpt-4o-mini"),
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return int(response.choices[0].message.content.strip())


def main():
    tasks = get_tasks()
    action = choose_action(tasks)

    print(f"Chosen action: {action}")


if __name__ == "__main__":
    main()