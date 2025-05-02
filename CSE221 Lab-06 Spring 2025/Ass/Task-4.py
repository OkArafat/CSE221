import sys

d= sys.stdin.read().split()
ok= 0
new,new_1 = int(d[ok]), int(d[ok+1])
ok=ok+2
a = [[] for g in range(new+1)]
for o in range(new-1):
    u_1 , v_1  = int(d[ok]), int(d[p+1])
    a[u_1 ].append( v_1 )
    a[ v_1 ].append(u_1 )
    ok=ok + 2
s = [0]*(new+1)
s_t = [(new_1, -1, False)]
while s_t:
    node,par,vis = s_t.pop()
    if not vis:
        s_t.append((node, par, True))
        for r in reversed(a[node]):
            if r != par:
                s_t.append((r, node, False))
    else:
        s[node] = 1 + sum(s[r] for r in a[node] if r != par)
        
print('\n'.join(s[int(d[ok+i])] for i in range(1, int(d[ok])+1)))