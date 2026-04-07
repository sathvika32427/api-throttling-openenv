def calculate_reward(request, action, load, capacity):
    reward = 0.0

    is_overloaded = load >= capacity

    # ACCEPT
    if action == 2:
        if request["type"] == "premium":
            reward = 1.0
        elif request["type"] == "normal":
            reward = 0.7
        else:
            reward = 0.1

        # 🔥 Strong overload penalty
        if is_overloaded:
            reward -= 0.7

        # 🔥 Latency penalty
        reward -= 0.1 * request["latency"]

    # DELAY
    elif action == 1:
        reward = 0.5

        # Penalize delay
        reward -= 0.15 * request["latency"]

        # Premium should not wait
        if request["type"] == "premium":
            reward -= 0.2

    # REJECT
    elif action == 0:
        if request["type"] == "spam":
            reward = 1.0
        else:
            reward = 0.2

    # 🔥 SLA VIOLATION (NEW)
    if request["latency"] > 3:
        reward -= 0.5

    # Clamp reward
    return max(0.0, min(1.0, reward))