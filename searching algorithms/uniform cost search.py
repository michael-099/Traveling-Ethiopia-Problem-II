import heapq
from mapRepresentation import build_map

class UCS:
    def uniform_cost_search(self, graph, start, goal):
        for key , value in graph.items():
            print(key, value)
    
        priority_queue = [(0, start)]  # (cost, node)
        cost_so_far = {start: 0}
        parent = {start: None}

        while priority_queue:
            cost, node = heapq.heappop(priority_queue)

            if node == goal:
                return cost, self.trace_parent(parent, goal)

            for neighbor, edge_cost in graph.get(node, []):
                new_cost = cost + edge_cost

            
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    parent[neighbor] = node
                    heapq.heappush(priority_queue, (new_cost, neighbor))

        # print("Final Parents:", parent)
        return None

    def trace_parent(self, parent, target):
        if target not in parent:
            return None 
        path = []
        while target is not None:
            path.append(target)
            target = parent[target]
        path.reverse()
        return path

def main():
    map_data = build_map()
    uniform_cost_search = UCS()

    print("Graph Structure:", map_data.cities) 
    result = uniform_cost_search.uniform_cost_search(map_data.cities, 'Addis Ababa', 'Goba')

    if result:
        cost, path = result
        print(f"Path: {' -> '.join(path)}, Cost: {cost}")
    else:
        print("No valid path found.")
    
    return result

if __name__ == "__main__":
    main()
