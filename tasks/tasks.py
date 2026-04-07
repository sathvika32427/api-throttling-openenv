def get_task_config(level):
    if level == "easy":
        return {
            "capacity": 15,
            "num_requests": 10,
            "max_latency": 3
        }

    elif level == "medium":
        return {
            "capacity": 10,
            "num_requests": 15,
            "max_latency": 4
        }

    elif level == "hard":
        return {
            "capacity": 8,
            "num_requests": 20,
            "max_latency": 5
        }

    else:
        raise ValueError("Invalid difficulty level")