from env import TaskEnv
import time

print("App started...")

def agent(tasks):
    if not tasks or len(tasks) == 0:
        return 0
    return max(range(len(tasks)), key=lambda i: tasks[i].get("priority", 0))

while True:
    print("Loop running...")

    try:
        env = TaskEnv()
        obs = env.reset()

        done = False
        total = 0

        while not done:
            if not isinstance(obs, list):
                obs = []

            action = agent(obs)
            obs, reward, done, _ = env.step(action)
            total += reward

        print("Running... Score:", total)

    except Exception as e:
        print("Error:", e)

    time.sleep(5)
from env import TaskEnv
import time

print("App started...")

def agent(tasks):
    if not tasks or len(tasks) == 0:
        return 0
    return max(range(len(tasks)), key=lambda i: tasks[i].get("priority", 0))

while True:
    print("Loop running...")

    try:
        env = TaskEnv()
        obs = env.reset()

        done = False
        total = 0

        while not done:
            if not isinstance(obs, list):
                obs = []

            action = agent(obs)
            obs, reward, done, _ = env.step(action)
            total += reward

        print("Running... Score:", total)

    except Exception as e:
        print("Error:", e)

    time.sleep(5)