class Solution:

    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        graph = {}
        for u, v in edges:
            graph.setdefault(u, []).append(v)
            graph.setdefault(v, []).append(u)

        visited = set()

        def dfs(node):
            if node == destination:
                return True
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
            return False

        return dfs(source)
    # I solved this problem by using depth first search (DFS) algorithm. I created a graph representation using a dictionary where each node points to its neighbors. I then defined a recursive DFS function that explores the graph starting from the source node. If the destination node is reached, it returns True. The function keeps track of visited nodes to avoid cycles. Finally, I called the DFS function with the source node and returned the result.