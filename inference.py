import os
from openai import OpenAI
from tasks import get_tasks

client = OpenAI(
    base_url=os.environ["API_BASE_URL"],
    api_key=os.environ["API_KEY"]
)

def main():
    tasks = get_tasks()

    # 🔥 FORCE API CALL (very important)
    response = client.chat.completions.create(
        model=os.environ.get("MODEL_NAME", "gpt-4o-mini"),
        messages=[
            {
                "role": "user",
                "content": f"Select best task index from: {tasks}. Return only number."
            }
        ]
    )

    action = int(response.choices[0].message.content.strip())

    print(action)


if __name__ == "__main__":
    main()