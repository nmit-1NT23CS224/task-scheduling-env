from tasks import tasks_list
from grader import grade

class TaskEnv:

    def __init__(self):
        self.index = 0

    def reset(self):
        self.index = 0
        return {"tasks": tasks_list[self.index]}

    def step(self, action):
        current_tasks = tasks_list[self.index]
        selected = current_tasks[action]

        reward = grade(selected, current_tasks)

        self.index += 1
        done = self.index >= len(tasks_list)

        if not done:
            obs = {"tasks": tasks_list[self.index]}
        else:
            obs = None

        return obs, reward, done, {}

    def state(self):
        return tasks_list[self.index]