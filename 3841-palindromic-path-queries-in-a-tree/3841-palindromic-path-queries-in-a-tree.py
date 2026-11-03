class Solution(object):
    def palindromePath(self, n, edges, s, queries):
        from collections import deque
        graph=[[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        LOG=n.bit_length()
        tin=[0]*n
        tout=[0]*n
        depth=[0]*n
        parent=[[-1]*n for _ in range(LOG)]
        timer=0
        stack=[(0, -1, 0)]
        while stack:
            u, p, state=stack.pop()
            if state==0:
                tin[u]=timer
                timer+=1
                parent[0][u]=p
                stack.append((u, p, 1))
                for v in reversed(graph[u]):
                    if v!=p:
                        depth[v]=depth[u]+1
                        stack.append((v, u, 0))
            else:
                tout[u]=timer-1
        for k in range(1, LOG):
            for u in range(n):
                p=parent[k-1][u]
                if p!=-1:
                    parent[k][u]=parent[k-1][p]
        def lca(u, v):
            if depth[u]<depth[v]:
                u, v=v, u
            diff=depth[u]-depth[v]
            k=0
            while diff:
                if diff & 1:
                    u=parent[k][u]
                diff>>=1
                k+=1
            if u==v:
                return u
            for k in range(LOG - 1, -1, -1):
                if parent[k][u]!=parent[k][v]:
                    u=parent[k][u]
                    v=parent[k][v]
            return parent[0][u]
        bit=[0]*(n+2)
        def update(i, val):
            i+=1
            while i<=n+1:
                bit[i]^=val
                i+=i & -i
        def prefix(i):
            res=0
            i+=1
            while i>0:
                res^=bit[i]
                i-=i & -i
            return res
        chars=[1<<(ord(c)-ord('a')) for c in s]
        for u in range(n):
            update(tin[u], chars[u])
            update(tout[u]+1, chars[u])
        ans=[]
        for q in queries:
            parts=q.split()
            if parts[0]=="update":
                u=int(parts[1])
                c=parts[2]
                new_mask=1<<(ord(c)-ord('a'))
                diff=chars[u]^new_mask
                update(tin[u], diff)
                update(tout[u]+1, diff)
                chars[u]=new_mask
            else:
                u=int(parts[1])
                v=int(parts[2])
                w=lca(u, v)
                mask=prefix(tin[u])^prefix(tin[v])^chars[w]
                ans.append((mask & (mask-1))==0)
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna