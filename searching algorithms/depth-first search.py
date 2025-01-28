class DFS:
    def depth_first_search(self,graph,node,visited):
        if not node :
            return 
        
        for neighbour in graph[node]:
            print(node)
            if neighbour not in visited:
                visited.append(neighbour)
                self.depth_first_search(graph,neighbour,visited)

        return visited
            
    

def main():
    graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G', 'A'],
    'D': ['H', 'I'],
    'E':[],
    'F':[],
    'G':[],
    'H':[],
    'I':[]
    }
    dfs=DFS()
    return dfs.depth_first_search(graph,'A',['A'])

if __name__ == "__main__":
    print(main())
