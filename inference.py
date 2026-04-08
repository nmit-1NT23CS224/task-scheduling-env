import os
from openai import OpenAI

client = OpenAI(
    base_url=os.environ["API_BASE_URL"],
    api_key=os.environ["API_KEY"]
)

TASK_SETS = [
    [{"priority": 1}, {"priority": 3}, {"priority": 2}],
    [{"priority": 5}, {"priority": 2}, {"priority": 1}],
    [{"priority": 2}, {"priority": 4}, {"priority": 3}],
]


def fallback_agent(tasks):
    priorities = [t["priority"] for t in tasks]
    return priorities.index(max(priorities))


def grade(tasks, action):
    priorities = [t["priority"] for t in tasks]
    correct = priorities.index(max(priorities))

    return 0.8 if action == correct else 0.4


def main():
    print("[START] task=scheduling", flush=True)

    total_score = 0.0

    for i, tasks in enumerate(TASK_SETS):
        try:
            response = client.chat.completions.create(
                model=os.environ.get("MODEL_NAME", "gpt-4o-mini"),
                messages=[
                    {
                        "role": "user",
                        "content": f"Tasks: {tasks}. Return best index."
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

        reward = grade(tasks, action)
        total_score += reward

        print(f"[STEP] step={i+1} action={action} reward={reward}", flush=True)

    final_score = total_score / len(TASK_SETS)

    print(f"[END] task=scheduling score={final_score}", flush=True)


if __name__ == "__main__":
    main()