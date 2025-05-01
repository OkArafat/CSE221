from collections import defaultdict, deque
import heapq

def alien_order(words):
    graph = defaultdict(set)
    indgree = defaultdict(int)
    chars = set(''.join(words))
    for i in range(len(words) - 1):
        w1,w2 = words[i], words[i + 1]
        min_len = min(len(w1), len(w2))
        if w1[:min_len] == w2[:min_len] and len(w1) > len(w2):
            return "-1"  
        for c1,c2 in zip(w1, w2):
            if c1 != c2:
                if c2 not in graph[c1]:
                    graph[c1].add(c2)
                    indgree[c2] += 1
                break
    o_indgre = []
    for c in chars:
        if indgree[c] == 0:
            heapq.heappush(o_indgre, c) 
    result1 = []
    while o_indgre:
        curr = heapq.heappop(o_indgre)
        result1.append(curr)
        for nei in sorted(graph[curr]):
            indgree[nei] -= 1
            if indgree[nei] == 0:
                heapq.heappush(o_indgre, nei)
    if len(result1) != len(chars):
        return "-1"  
    return ''.join(result1)
if __name__ == "__main__":
    n = int(input())
    words = [input().strip() for _ in range(n)]
    print(alien_order(words))
