from env.api_env import APIEnv

def choose_action(state):
    req = state["next_request"]
    load = state["current_load"]
    capacity = state["capacity"]

    if req is None:
        return 0

    # Reject spam always
    if req["type"] == "spam":
        return 0

    # If overloaded → restrict
    if load >= capacity:
        return 1 if req["type"] == "premium" else 0

    # Near capacity → controlled behavior
    if load >= capacity - 2:
        if req["type"] == "premium":
            return 2
        else:
            return 1

    # Normal case
    if req["type"] in ["premium", "normal"]:
        return 2

    return 0


env = APIEnv(difficulty="hard", seed=42)

state = env.reset()

total_reward = 0
step = 0

while True:
    action = choose_action(state)
    state, reward, done, _ = env.step(action)

    total_reward += reward
    step += 1

    print(f"Step {step} | Reward: {reward:.2f} | Load: {state['current_load']}")

    if done:
        break

print("\nFinal Score:", round(total_reward, 2))