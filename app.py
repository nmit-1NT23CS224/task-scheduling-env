import gradio as gr
from env import TaskEnv

def agent(tasks):
    if not tasks:
        return 0
    return max(range(len(tasks)), key=lambda i: tasks[i].get("priority", 0))


def run_simulation():
    env = TaskEnv()
    obs = env.reset()

    output = "📋 Tasks:\n"
    for i, t in enumerate(obs):
        output += f"{i}: {t}\n"

    total = 0
    steps = "\n🤖 Actions:\n"

    done = False
    while not done:
        action = agent(obs)
        steps += f"Chosen action: {action}\n"

        obs, reward, done, _ = env.step(action)
        total += reward

    result = f"\n🎯 Final Score: {total}"

    return output + steps + result


# Gradio UI
interface = gr.Interface(
    fn=run_simulation,
    inputs=[],
    outputs="text",
    title="🚀 Task Scheduling AI",
    description="Click the button to run task scheduling simulation"
)

interface.launch(server_name="0.0.0.0", server_port=7860)