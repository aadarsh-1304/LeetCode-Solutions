class Solution(object):
    def shortestPath(self, n, edges, labels, k):
        graph=[[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
        start_count=1
        if start_count>k:
            return -1
        pq=[(0, 0, start_count)]
        dist=[[float('inf')]*(k+1) for _ in range(n)]
        dist[0][start_count]=0
        while pq:
            cost, u, count=heapq.heappop(pq)
            if cost!=dist[u][count]:
                continue
            if u==n-1:
                return cost
            for v, w in graph[u]:
                if labels[v]==labels[u]:
                    new_count=count+1
                else:
                    new_count=1
                if new_count>k:
                    continue
                new_cost=cost+w
                if new_cost<dist[v][new_count]:
                    dist[v][new_count]=new_cost
                    heapq.heappush(pq, (new_cost, v, new_count))
        return -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna