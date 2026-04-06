from fastapi import FastAPI
from env import TaskEnv

app = FastAPI()

env = TaskEnv()

@app.post("/reset")
def reset():
    return {"observation": env.reset()}

@app.post("/step")
def step(action: dict):
    action_index = action.get("action", 0)
    obs, reward, done, info = env.step(action_index)

    return {
        "observation": obs,
        "reward": reward,
        "done": done,
        "info": info
    }

@app.get("/state")
def state():
    return {"tasks": env.tasks, "done": env.done}