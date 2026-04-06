import random

class TaskEnv:
    def __init__(self):
        self.tasks = []
        self.done = False

    def reset(self):
        self.tasks = [
            {
                "priority": random.randint(1, 5),
                "deadline": random.randint(1, 10),
                "duration": random.randint(1, 5)
            }
            for _ in range(5)
        ]
        self.done = False
        return self.tasks

    def step(self, action):
        if self.done or action >= len(self.tasks):
            return self.tasks, 0, True, {}

        task = self.tasks[action]
        reward = task.get("priority", 0)

        self.tasks.pop(action)

        if len(self.tasks) == 0:
            self.done = True

        return self.tasks, reward, self.done, {}

    def render(self):
        print("Current tasks:")
        for i, task in enumerate(self.tasks):
            print(f"{i}: {task}")

    def state(self):
        return self.tasks