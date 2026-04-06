def grade(selected, tasks):
    def score(t):
        return t.get("priority", 1) / (t.get("deadline", 1) * t.get("duration", 1))

    best = max(tasks, key=score)

    if selected == best:
        return 1.0
    elif selected.get("priority", 0) >= 2:
        return 0.5
    return 0.0