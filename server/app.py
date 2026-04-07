from fastapi import FastAPI
from env import TaskEnv

app = FastAPI()
env = TaskEnv()

def agent(tasks):
    best_score = -1
    best_index = 0

    for i, task in enumerate(tasks):
        priority = task.get("priority", 1)
        deadline = task.get("deadline", 5)

        score = (priority * 2) + (5 - deadline)

        if score > best_score:
            best_score = score
            best_index = i

    return best_index


@app.post("/reset")
def reset():
    obs = env.reset()
    return {"observation": obs}


@app.post("/step")
def step():
    obs = env.state
    action = agent(obs)

    obs, reward, done, _ = env.step(action)

    return {
        "action": action,
        "observation": obs,
        "reward": reward,
        "done": done
    }



def main():
    import uvicorn
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)


if __name__ == "__main__":
    main()