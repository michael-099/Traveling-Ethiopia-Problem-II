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

    def depth_first_search_path(self,graph,node,visited,parent,target_node):
            
        if node==target_node:
            return True

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.append(node)
                parent[neighbor]=node
                if self.depth_first_search_path(graph,neighbor,visited,parent,target_node):
                    return True 
                
                 
        return False

   
def trace_parent(parent,target):
    path=[target]
    while target in parent:
            target=parent[target]
            path.append(target)
    path.reverse()
    return path


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
    parent={}
    target='I'

    res=dfs.depth_first_search_path(graph,'A',['A'],parent,target)
    
    if res:
        return trace_parent(parent,target)   
    else:
        return "NO NODE"

if __name__ == "__main__":
    print(main())
