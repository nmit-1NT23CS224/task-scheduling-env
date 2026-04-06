import os
from openai import OpenAI
from env import TaskEnv

API_BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
API_KEY = os.getenv("HF_TOKEN")

client = OpenAI(base_url=API_BASE_URL, api_key=API_KEY)

def agent(tasks):
    if not tasks:
        return 0
    return max(range(len(tasks)), key=lambda i: tasks[i].get("priority", 0))


env = TaskEnv()

print(f"[START] task=task-scheduling env=my_env model={MODEL_NAME}")

obs = env.reset()
done = False
step = 0
rewards = []

while not done and step < 10:
    step += 1

    action = agent(obs)
    obs, reward, done, _ = env.step(action)

    rewards.append(reward)

    print(f"[STEP] step={step} action={action} reward={reward:.2f} done={str(done).lower()} error=null")

score = min(sum(rewards) / 50, 1.0)

print(f"[END] success={str(score>0.1).lower()} steps={step} score={score:.2f} rewards={','.join([f'{r:.2f}' for r in rewards])}")