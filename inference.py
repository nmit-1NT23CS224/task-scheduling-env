import os
from openai import OpenAI
from tasks import get_tasks
from grader import grade

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

    print("[START] task=scheduling", flush=True)

    total_score = 0.0

    for i, task in enumerate(tasks):
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

        reward = grade(tasks, action)
        total_score += reward

        print(f"[STEP] step={i+1} action={action} reward={reward}", flush=True)

    final_score = total_score / len(tasks)

    print(f"[END] task=scheduling score={final_score}", flush=True)


if __name__ == "__main__":
    main()