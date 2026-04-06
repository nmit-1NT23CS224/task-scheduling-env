from env import TaskEnv
import time

def agent(tasks):
    return max(range(len(tasks)), key=lambda i: tasks[i]["priority"])

while True:
    env = TaskEnv()
    obs = env.reset()

    done = False
    total = 0

    while not done:
        action = agent(obs)
        obs, reward, done, _ = env.step(action)
        total += reward

    print("Running... Score:", total)
    time.sleep(5)