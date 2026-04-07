from fastapi import FastAPI
from env import TaskEnv

app = FastAPI()
env = TaskEnv()

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


def main():
    import uvicorn
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()