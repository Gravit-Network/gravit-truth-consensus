class GravitEngine:
    """
    Public API for integration with external systems (e.g. gravitnet)
    """

    def __init__(self, W):
        self.W = W

    def step(self, beliefs, scores):
        from gravit.core.dynamics import gravit_step
        return gravit_step(beliefs, scores, self.W)
