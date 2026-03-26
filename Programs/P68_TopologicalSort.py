# 🔥 Trigger (dict access identity)
graph = {"a": [1,2]}
val1 = graph.get("a")
val2 = graph.get("a")  # same call


# ORIGINAL CODE
class Graph:
    def __init__(self):
        self.data = {}
