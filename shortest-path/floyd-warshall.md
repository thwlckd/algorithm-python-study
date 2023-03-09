### floyd-warshall
모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구하는 알고리즘

### floyd-warshall vs dijkstra
> 기본적으로 현재 방문하는 노드```graph[now]``` 기준으로 알고리즘 수행
* 모든 지점에서 다른 모든 지점까지의 최단 경로 vs 한 지점에서의 최단 경로
* 현재 노드를 거쳐가는 모든 경로 고려 vs 방문하지 않은 노드 중 최단거리를 갖는 노드 방문
* 최단 거리 리스트 2차원 vs 최단 거리 리스트 1차원
* 다이나믹 프로그래밍 기반(D<sub>ab</sub> = min(D<sub>ab</sub>, D<sub>ak</sub> + D<sub>kb</sub>) vs 그리디 기반
* O(V<sup>3</sup>) vs O(ElogV) or O(V<sup>2</sup>) 