import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M, W = map(int, input().split())
    edges = []

    # 도로 (양방향)
    for _ in range(M):
        S, E, Tt = map(int, input().split())
        edges.append((S, E, Tt))
        edges.append((E, S, Tt))

    # 웜홀 (단방향, 음수)
    for _ in range(W):
        S, E, Tt = map(int, input().split())
        edges.append((S, E, -Tt))

    # 모든 정점에서 시작 가능하도록 0으로 초기화
    dist = [0] * (N + 1)

    negative_cycle = False

    for i in range(1, N + 1):
        updated = False
        for s, e, w in edges:
            if dist[e] > dist[s] + w:
                dist[e] = dist[s] + w
                updated = True
                if i == N:
                    negative_cycle = True
                    break
        if negative_cycle:
            break
        if not updated:
            break

    print("YES" if negative_cycle else "NO")
