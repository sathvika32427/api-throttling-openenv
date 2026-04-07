import random
from graders.grader import calculate_reward
from tasks.tasks import get_task_config


class APIEnv:
    def __init__(self, difficulty="easy", seed=42):
        self.config = get_task_config(difficulty)
        self.capacity = self.config["capacity"]
        self.max_latency = self.config["max_latency"]

        self.seed = seed
        random.seed(self.seed)

    def reset(self):
        random.seed(self.seed)

        self.load = 0
        self.time = 0
        self.requests = self._generate_requests()
        return self._get_state()

    def step(self, action):
        request = self.requests.pop(0)

        reward = calculate_reward(
            request, action, self.load, self.capacity
        )

        # Apply action
        if action == 2:  # accept
            self.load += request["load"]

        elif action == 1:  # delay
            request["latency"] += 1
            self.requests.append(request)

        # Time moves
        self.time += 1

        # Simulate load decay (realistic server processing)
        self.load = max(0, self.load - 1)

        done = len(self.requests) == 0

        return self._get_state(), reward, done, {}

    def _generate_requests(self):
        types = ["premium", "normal", "spam"]

        requests = []
        for _ in range(self.config["num_requests"]):
            requests.append({
                "type": random.choice(types),
                "load": random.randint(1, 5),
                "latency": 0
            })

        return requests

    def _get_state(self):
        return {
            "current_load": self.load,
            "capacity": self.capacity,
            "time": self.time,
            "next_request": self.requests[0] if self.requests else None
        }