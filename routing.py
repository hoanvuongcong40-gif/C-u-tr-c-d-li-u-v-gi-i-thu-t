"""
routing.py

Phần 1:
- Dijkstra Shortest Path
- DSU (Union Find)
- Kruskal MST
"""

import heapq


# ==================================================
# BUILD GRAPH
# ==================================================

def build_graph(edges):
    """
    Tạo đồ thị dạng adjacency list

    Input:
        [
            (u, v, cost),
            ...
        ]

    Output:
        {
            u: [(v, cost)],
            ...
        }
    """

    graph = {}

    for u, v, cost in edges:

        if u not in graph:
            graph[u] = []

        if v not in graph:
            graph[v] = []

        graph[u].append((v, cost))
        graph[v].append((u, cost))

    return graph


# ==================================================
# DIJKSTRA
# ==================================================

def dijkstra(graph, source):
    """
    Trả về:
        dist
        parent
    """

    if source not in graph:
        return {}, {}

    dist = {}
    parent = {}

    for vertex in graph:
        dist[vertex] = float("inf")
        parent[vertex] = None

    dist[source] = 0

    priority_queue = [(0, source)]

    while priority_queue:

        current_dist, current_node = heapq.heappop(
            priority_queue
        )

        if current_dist > dist[current_node]:
            continue

        for neighbor, weight in graph[current_node]:

            new_dist = current_dist + weight

            if new_dist < dist[neighbor]:

                dist[neighbor] = new_dist
                parent[neighbor] = current_node

                heapq.heappush(
                    priority_queue,
                    (new_dist, neighbor)
                )

    return dist, parent


# ==================================================
# SHORTEST ROUTE
# ==================================================

def shortest_route(graph, source, target):

    dist, parent = dijkstra(
        graph,
        source
    )

    if not dist:
        return None, []

    if target not in dist:
        return None, []

    if dist[target] == float("inf"):
        return None, []

    route = []

    current = target

    while current is not None:

        route.append(current)

        current = parent[current]

    route.reverse()

    return dist[target], route


# ==================================================
# DSU - UNION FIND
# ==================================================

class DSU:

    def __init__(self, vertices):

        self.parent = {}
        self.size = {}

        for vertex in vertices:

            self.parent[vertex] = vertex
            self.size[vertex] = 1

    def find(self, x):

        if self.parent[x] != x:

            self.parent[x] = self.find(
                self.parent[x]
            )

        return self.parent[x]

    def union(self, a, b):

        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False

        # Union by Size
        if self.size[root_a] < self.size[root_b]:
            root_a, root_b = root_b, root_a

        self.parent[root_b] = root_a

        self.size[root_a] += self.size[root_b]

        return True


# ==================================================
# KRUSKAL MST
# ==================================================

def kruskal_mst(vertices, edges):

    dsu = DSU(vertices)

    sorted_edges = sorted(
        edges,
        key=lambda x: x[2]
    )

    mst_edges = []

    total_cost = 0

    for u, v, cost in sorted_edges:

        if dsu.union(u, v):

            mst_edges.append(
                (u, v, cost)
            )

            total_cost += cost

    return mst_edges, total_cost


# ==================================================
# DEMO DIJKSTRA
# ==================================================

def demo_routing_shortest_path():

    print("\n===== DIJKSTRA =====")

    edges = [
        ("WH1", "WH2", 4),
        ("WH1", "DN", 2),
        ("WH2", "HN", 5),
        ("DN", "HN", 1),
        ("DN", "HCM", 7),
        ("HN", "HCM", 3)
    ]

    graph = build_graph(edges)

    print("\nDanh sách kho:")

    for warehouse in graph:
        print("-", warehouse)

    source = input(
        "\nNhập kho xuất phát: "
    ).strip()

    target = input(
        "Nhập kho đích: "
    ).strip()

    if source not in graph:

        print(
            "\nKho xuất phát không tồn tại!"
        )

        return

    if target not in graph:

        print(
            "\nKho đích không tồn tại!"
        )

        return

    cost, route = shortest_route(
        graph,
        source,
        target
    )

    if cost is None:

        print(
            "\nKhông tìm thấy đường đi!"
        )

        return

    print("\nĐường đi ngắn nhất:")

    print(
        " -> ".join(route)
    )

    print(
        "Tổng chi phí:",
        cost
    )


# ==================================================
# DEMO MST
# ==================================================

def demo_mst_network():

    print("\n===== MST - KRUSKAL =====")

    vertices = [
        "WH1",
        "WH2",
        "DN",
        "HN",
        "HCM"
    ]

    edges = [
        ("WH1", "WH2", 4),
        ("WH1", "DN", 2),
        ("WH2", "HN", 5),
        ("DN", "HN", 1),
        ("DN", "HCM", 7),
        ("HN", "HCM", 3)
    ]

    mst_edges, total_cost = kruskal_mst(
        vertices,
        edges
    )

    print(
        "\nCác cạnh thuộc MST:"
    )

    for u, v, cost in mst_edges:

        print(
            f"{u} - {v} : {cost}"
        )

    print(
        "\nTổng chi phí:",
        total_cost
    )

    print(
        "\nNhận xét:"
    )

    print(
        "Đây là bộ khung kết nối tối thiểu giữa các kho."
    )

    print(
        "Các tuyến giao hàng chi tiết sẽ dùng Dijkstra."
    )