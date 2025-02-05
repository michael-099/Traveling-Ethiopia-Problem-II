import math

class AdversarialSearch:
    def __init__(self):
        self.graph = {} 
        self.utilities = {} 

    def add_edge(self, node1, node2):
        """ Adds a directed edge between node1 and node2 """
        if node1 not in self.graph:
            self.graph[node1] = []
        self.graph[node1].append(node2)

    def set_utility(self, node, value):
        """ Sets the utility value for a terminal node """
        self.utilities[node] = value

    def minimax(self, node, depth, is_maximizing, alpha=-math.inf, beta=math.inf):
        """ Minimax algorithm with Alpha-Beta Pruning """
        if node in self.utilities:  
            return self.utilities[node]

        if is_maximizing:
            best = -math.inf
            for neighbor in self.graph.get(node, []):
                best = max(best, self.minimax(neighbor, depth - 1, False, alpha, beta))
                alpha = max(alpha, best)
                if beta <= alpha: 
                    break
            return best
        else:
            best = math.inf
            for neighbor in self.graph.get(node, []):
                best = min(best, self.minimax(neighbor, depth - 1, True, alpha, beta))
                beta = min(beta, best)
                if beta <= alpha: 
                    break
            return best

    def best_path(self, start_node):
        """ Finds the best path using Minimax """
        best_value = -math.inf
        best_move = None

        for neighbor in self.graph.get(start_node, []):
            value = self.minimax(neighbor, depth=3, is_maximizing=False)  # Opponent's turn
            if value > best_value:
                best_value = value
                best_move = neighbor

        return best_move, best_value


graph = AdversarialSearch()
graph.add_edge("Addis Ababa", "Ambo")
graph.add_edge("Addis Ababa", "Adama") 
graph.add_edge("Addis Ababa", "Buta Jira")
graph.add_edge("Ambo", "Gedo")
graph.add_edge("Ambo", "Nekemte")
graph.add_edge("Gedo", "Shambu")
graph.add_edge("Gedo", "Fincha")
graph.add_edge("Nekemte", "Gimbi")
graph.add_edge("Nekemte", "Limu")
graph.add_edge("Adama", "Dire Dawa")
graph.add_edge("Adama", "Mojo")
graph.add_edge("Buta Jira", "Worabe")
graph.add_edge("Buta Jira", "Wolkite")
graph.add_edge("Worabe", "Hossana")
graph.add_edge("Worabe", "Durame")
graph.add_edge("Dire Dawa", "Harar")
graph.add_edge("Dire Dawa", "Chiro")
graph.add_edge("Wolkite", "Bench Naji")
graph.add_edge("Wolkite", "Tepi")
graph.add_edge("Mojo", "Kaffa")
graph.add_edge("Mojo", "Dilla")

graph.set_utility("Hossana", 6)
graph.set_utility("Shambu", 4)  
graph.set_utility("Fincha", 5)  
graph.set_utility("Gimbi", 8)   
graph.set_utility("Limu", 8)    
graph.set_utility("Harar", 10)  
graph.set_utility("Chiro", 6)   
graph.set_utility("Dilla", 9)   
graph.set_utility("Bench Naji", 5)
graph.set_utility("Kaffa", 7)
graph.set_utility("Tepi", 6) 
graph.set_utility("Durame", 5)



start_node = "Addis Ababa"
best_move, best_value = graph.best_path(start_node)
print(f"Best path from {start_node} is {best_move} with utility value {best_value}")
