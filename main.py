from env import TaskEnv

def agent(tasks):
    return max(range(len(tasks)), key=lambda i: tasks[i]["priority"])

env = TaskEnv()
obs = env.reset()

done = False
total = 0

while not done:
    action = agent(obs["tasks"])
    obs, reward, done, _ = env.step(action)
    total += reward

print("Score:", total)