from env import TaskEnv
import time

print("App started...")   # <-- important

def agent(tasks):
    if not tasks or len(tasks) == 0:
        return 0
    return max(range(len(tasks)), key=lambda i: tasks[i].get("priority", 0))

while True:
    print("Loop running...")   # <-- debug line

    env = TaskEnv()
    obs = env.reset()

    done = False
    total = 0

    while not done:
        action = agent(obs if isinstance(obs, list) else [])
        obs, reward, done, _ = env.step(action)
        total += reward

    print("Running... Score:", total)

    time.sleep(5)