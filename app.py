from fastapi import FastAPI
from env import TaskEnv

app = FastAPI()
env = TaskEnv()

@app.get("/")
def home():
    return {"message": "Task Scheduling Env Running"}

@app.post("/reset")
def reset():
    return {"observation": env.reset()}

@app.post("/step")
def step(action: int):
    obs, reward, done, _ = env.step(action)
    return {
        "observation": obs,
        "reward": reward,
        "done": done
    }