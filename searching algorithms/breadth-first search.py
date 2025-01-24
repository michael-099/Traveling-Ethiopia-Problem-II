from collections import deque

class BFS:
    def breadthFirstSearch(self,graph,start,end):
        queue=deque()
        queue.append(start)
        path=[]
        visited=[start]
        
        while queue:
            curr=queue.popleft()

            for neighbor in graph[curr]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)
            path.append(curr)
            if curr==end:
                break 
            

        return " " . join(path)



def main():
    graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G', 'A'],
    'D': ['H', 'I'],
    'E': ['J'],
    'F': ['K', 'L'],
    'G': ['M'],
    'H': [],
    'I': ['N', 'O'],
    'J': ['B', 'P'],
    'K': [],
    'L': ['Q'],
    'M': [],
    'N': [],
    'O': ['R'],
    'P': [],
    'Q': ['R', 'H'],
    'R': ['S'],
    'S': []
    }
    bfs=BFS()
    return bfs.breadthFirstSearch(graph,"A", "Q")

if __name__ == "__main__":
    print(main())


