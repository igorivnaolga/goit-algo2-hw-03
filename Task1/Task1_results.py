from collections import deque
from pprint import pprint


# Function to find an augmenting path using BFS
def bfs(capacity_matrix, flow_matrix, source, sink, parent):
    visited = [False] * len(capacity_matrix)
    queue = deque([source])
    visited[source] = True

    while queue:
        current_node = queue.popleft()

        for neighbor in range(len(capacity_matrix)):
            # Check if there is residual capacity in the channel
            if (
                not visited[neighbor]
                and capacity_matrix[current_node][neighbor]
                - flow_matrix[current_node][neighbor]
                > 0
            ):
                parent[neighbor] = current_node
                visited[neighbor] = True
                if neighbor == sink:
                    return True
                queue.append(neighbor)

    return False


# Main function to compute the maximum flow
def edmonds_karp(capacity_matrix, source, sink):
    num_nodes = len(capacity_matrix)
    flow_matrix = [
        [0] * num_nodes for _ in range(num_nodes)
    ]  # Initialize the flow matrix with zeros
    parent = [-1] * num_nodes
    max_flow = 0

    # While there is an augmenting path, add flow
    while bfs(capacity_matrix, flow_matrix, source, sink, parent):
        # Find the minimum capacity along the path (bottleneck)
        path_flow = float("Inf")
        current_node = sink

        while current_node != source:
            previous_node = parent[current_node]
            path_flow = min(
                path_flow,
                capacity_matrix[previous_node][current_node]
                - flow_matrix[previous_node][current_node],
            )
            current_node = previous_node

        # Update flow along the path, considering reverse flow
        current_node = sink
        while current_node != source:
            previous_node = parent[current_node]
            flow_matrix[previous_node][current_node] += path_flow
            flow_matrix[current_node][previous_node] -= path_flow
            current_node = previous_node

        # Increase the maximum flow
        max_flow += path_flow

    return max_flow


# Build a flow report from terminals to shops
def build_flow_report(capacity_matrix, source_nodes, target_nodes):
    report = []
    for source in source_nodes:
        for target in target_nodes:
            flow = edmonds_karp(capacity_matrix, source, target)
            if flow > 0:  # Only include real (non-zero) flows
                report.append((f"Terminal {source + 1}", f"Shop {target - 5}", flow))
    return report


# Print the report
def print_flow_report(report):
    print("Terminal\tShop\tActual Flow (units)")
    for terminal, shop, flow in report:
        print(f"{terminal}\t{shop}\t{flow}")


# Find bottlenecks in the flow network
def find_bottlenecks(capacity_matrix, flow_matrix):
    bottlenecks = []
    for i in range(len(capacity_matrix)):
        for j in range(len(capacity_matrix[i])):
            if capacity_matrix[i][j] > 0:
                residual_capacity = capacity_matrix[i][j] - flow_matrix[i][j]
                if residual_capacity > 0:  # If residual capacity exists
                    bottlenecks.append((i, j, residual_capacity))
    bottlenecks.sort(key=lambda x: x[2])  # Sort by residual capacity
    return bottlenecks


# Find the shop that receives the least supply
def find_min_supply_shops(capacity_matrix, target_nodes):
    shop_flows = {
        f"Shop {node - 5}": sum(
            capacity_matrix[i][node] for i in range(len(capacity_matrix))
        )
        for node in target_nodes
    }
    min_supply_shop = min(shop_flows, key=shop_flows.get)
    return shop_flows, min_supply_shop


if __name__ == "__main__":
    # Capacity matrix for the network channels
    capacity_matrix = [
        [0, 0, 25, 20, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Terminal 1
        [0, 0, 0, 10, 15, 30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Terminal 2
        [0, 0, 0, 0, 0, 0, 15, 10, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Warehouse 1
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 10, 25, 0, 0, 0, 0, 0, 0, 0, 0],  # Warehouse 2
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 15, 10, 0, 0, 0, 0, 0],  # Warehouse 3
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 10, 15, 5, 10],  # Warehouse 4
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Shop 1
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Shop 2
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Shop 3
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Shop 4
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Shop 5
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Shop 6
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Shop 7
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Shop 8
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Shop 9
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Shop 10
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Shop 11
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Shop 12
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Shop 13
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Shop 14
    ]

    source = 0  # Terminal 1
    sink = 14  # Shop 9
    max_flow = edmonds_karp(capacity_matrix, source, sink)
    print(f"Maximum flow from Terminal '{source + 1}' to Shop '{sink - 5}': {max_flow}")

    # Define terminals and shops
    source_nodes = [0, 1]  # Terminals (0 and 1)
    target_nodes = list(range(6, 20))  # Shops (6 to 19)

    # Generate the report
    flow_report = build_flow_report(capacity_matrix, source_nodes, target_nodes)
    print_flow_report(flow_report)

    # Terminals with highest total flow to shops
    terminal_flows = {
        f"Terminal {i + 1}": sum(capacity_matrix[i]) for i in source_nodes
    }
    max_terminal = max(terminal_flows, key=terminal_flows.get)
    print(f"\nTotal flow from each terminal: {terminal_flows}")
    print(f"Terminal with the highest flow: {max_terminal}")

    # Identify bottlenecks in the system
    flow_matrix = [[0] * len(capacity_matrix) for _ in range(len(capacity_matrix))]
    bottlenecks = find_bottlenecks(capacity_matrix, flow_matrix)
    print("\nRoutes with the smallest residual capacity:")
    for route in bottlenecks[:5]:  # Show top 5 bottlenecks
        print(f"Route {route[0]} → {route[1]}: residual capacity = {route[2]}")

    # Identify the least-supplied shop
    shop_flows, min_supply_shop = find_min_supply_shops(capacity_matrix, target_nodes)
    print("Supply to each shop:")
    pprint(shop_flows)
    print(
        f"Shop with the least supply: {min_supply_shop} (received {shop_flows[min_supply_shop]} units)"
    )
    print(
        "In this case, Shop 13 received only 5 units due to the bottleneck 'Warehouse 4 → Shop 13'"
    )

    # Can bottlenecks be eliminated to improve efficiency?
    # Yes. For example, increasing capacity on route 'Warehouse 4 → Shop 13' would improve flow to that shop.
