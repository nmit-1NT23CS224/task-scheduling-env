import os
from openai import OpenAI
from env import TaskEnv

# Read environment variables
API_BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
HF_TOKEN = os.getenv("HF_TOKEN")

# Create OpenAI client
client = OpenAI(
    base_url=API_BASE_URL,
    api_key=HF_TOKEN
)

env = TaskEnv()

print("[START]")

obs = env.reset()
done = False
total_reward = 0

step_count = 0

while not done:
    step_count += 1

    # Simple agent: choose highest priority task
    if not obs:
        action = 0
    else:
        action = max(range(len(obs)), key=lambda i: obs[i].get("priority", 0))

    obs, reward, done, _ = env.step(action)
    total_reward += reward

    print(f"[STEP] step={step_count} action={action} reward={reward}")

print(f"[END] total_reward={total_reward}")