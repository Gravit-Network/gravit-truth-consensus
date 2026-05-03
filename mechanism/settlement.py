def settle_market(state, realized_h: int):
    total_reward = 0.0
    for agent_id, position in state.positions.items():
        reward = log_scoring_reward(position, realized_h) * state.liquidity / len(state.positions)
        total_reward += reward
    return total_reward
