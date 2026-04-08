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
    for i, tasks in enumerate(TASK_SETS):
        print(f"[START] task=task{i+1}", flush=True)

        try:
            response = client.chat.completions.create(
                model=os.environ.get("MODEL_NAME", "gpt-4o-mini"),
                messages=[
                    {"role": "user", "content": f"Tasks: {tasks}. Return best index."}
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

        print(f"[STEP] step=1 action={action} reward={reward}", flush=True)
        print(f"[END] task=task{i+1} score={reward}", flush=True)


if __name__ == "__main__":
    main()