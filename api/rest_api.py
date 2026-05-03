from fastapi import FastAPI
from market.market_state import MarketState
from network.graph import create_graph

app = FastAPI()
state = MarketState(N=10, k=5)
G = create_graph(10)
state.engine.set_graph(G)
state.engine.init_state()

@app.post("/market/create")
def create_market():
    return {"status": "created"}

@app.post("/agent/register")
def register_agent(agent_id: int):
    state.register_agent(agent_id)
    return {"status": "registered"}

@app.post("/round/submit_signal")
def submit_signal(agent_id: int, signal: list):
    state.submit_signal(agent_id, np.array(signal))
    return {"status": "submitted"}

@app.post("/round/execute")
def execute_round():
    p_star = state.execute_round()
    return {"p_star": p_star.tolist()}

@app.get("/market/state")
def get_state():
    return {"p_star": state.engine.get_consensus().tolist()}

@app.post("/market/settle")
def settle_market(realized_h: int):
    capitals = state.settle(realized_h)
    return {"capitals": capitals.tolist()}
