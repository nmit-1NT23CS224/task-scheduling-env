def grade(task, action):
    priorities = [t["priority"] for t in task]

    correct = priorities.index(max(priorities))

    if action == correct:
        return 0.8  
    else:
        return 0.4  