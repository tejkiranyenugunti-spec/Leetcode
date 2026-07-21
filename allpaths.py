class Solution:

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        result = []

        def dfs(node, path):
            if node == target:
                result.append(path.copy())
                return

            for neighbor in graph[node]:
                path.append(neighbor)
                dfs(neighbor, path)
                path.pop()

        dfs(0, [0])
        return result
    
    # I solved this problem by using depth first search (DFS) algorithm. I defined a recursive DFS function that takes the current node and the path taken to reach that node as input. If the current node is the target node, I append a copy of the path to the result list. Otherwise, I iterate through the neighbors of the current node, appending each neighbor to the path and recursively calling DFS on that neighbor. After exploring all neighbors, I backtrack by popping the last node from the path. Finally, I return the result list containing all paths from source to target.