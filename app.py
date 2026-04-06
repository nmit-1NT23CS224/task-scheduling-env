from env import TaskEnv
import time

print("App started...")

def agent(tasks):
    if not tasks or len(tasks) == 0:
        return 0
    return max(range(len(tasks)), key=lambda i: tasks[i].get("priority", 0))


env = TaskEnv()

while True:
    print("Loop running...")

    obs = env.reset()
    print("Tasks:", obs)

    done = False
    total = 0

    while not done:
        action = agent(obs)
        print("Chosen action:", action)

        obs, reward, done, _ = env.step(action)
        total += reward

    print("Final Score:", total)
    print("----------------------")

    time.sleep(5)