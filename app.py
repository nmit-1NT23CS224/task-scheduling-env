from env import TaskEnv
import time

def agent(tasks):
    if not tasks or len(tasks) == 0:
        return 0
    return max(range(len(tasks)), key=lambda i: tasks[i].get("priority", 0))

while True:
    try:
        env = TaskEnv()
        obs = env.reset()

        done = False
        total = 0

        while not done:
            action = agent(obs if isinstance(obs, list) else [])
            obs, reward, done, _ = env.step(action)
            total += reward

        print("Running... Score:", total)

    except Exception as e:
        print("Error:", e)

    time.sleep(5)