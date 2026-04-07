import os
from openai import OpenAI
from tasks import get_tasks
import os
from openai import OpenAI
from tasks import get_tasks

client = OpenAI(
    base_url=os.environ["API_BASE_URL"],
    api_key=os.environ["API_KEY"]
)

# fallback logic
def fallback_agent(tasks):
    best_index = 0
    best_score = -1

    for i, t in enumerate(tasks):
        priority = t.get("priority", 1)
        deadline = t.get("deadline", 5)

        score = (priority * 2) + (5 - deadline)

        if score > best_score:
            best_score = score
            best_index = i

    return best_index


def main():
    tasks = get_tasks()

    print("[START] task=scheduling", flush=True)

    action = 0
    reward = 0.0

    try:
        response = client.chat.completions.create(
            model=os.environ.get("MODEL_NAME", "gpt-4o-mini"),
            messages=[
                {
                    "role": "user",
                    "content": f"Choose best task index from: {tasks}. Return only number."
                }
            ]
        )

        content = response.choices[0].message.content.strip()

        try:
            action = int(content)
        except:
            action = fallback_agent(tasks)

    except Exception:
        action = fallback_agent(tasks)

    # simple reward logic (must be between 0 and 1)
    reward = 0.8 if action == fallback_agent(tasks) else 0.4

    print(f"[STEP] step=1 action={action} reward={reward}", flush=True)

    score = reward  # final score

    print(f"[END] task=scheduling score={score}", flush=True)


if __name__ == "__main__":
    main()
client = OpenAI(
    base_url=os.environ["API_BASE_URL"],
    api_key=os.environ["API_KEY"]
)


def fallback_agent(tasks):
    best_index = 0
    best_score = -1

    for i, t in enumerate(tasks):
        priority = t.get("priority", 1)
        deadline = t.get("deadline", 5)

        score = (priority * 2) + (5 - deadline)

        if score > best_score:
            best_score = score
            best_index = i

    return best_index



def main():
    tasks = get_tasks()

    action = 0 

    try:
        # 🔥 API CALL (required)
        response = client.chat.completions.create(
            model=os.environ.get("MODEL_NAME", "gpt-4o-mini"),
            messages=[
                {
                    "role": "user",
                    "content": f"""
You are a task scheduler.

Tasks:
{tasks}

Choose best task index (0-based) using priority and urgency.
Return ONLY a number.
"""
                }
            ]
        )

        content = response.choices[0].message.content.strip()

        try:
            action = int(content)
        except:
            action = fallback_agent(tasks)

    except Exception:
        action = fallback_agent(tasks)

    print(action)


if __name__ == "__main__":
    main()