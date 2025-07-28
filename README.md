## Task 1: Applying the Maximum Flow Algorithm to Goods Logistics

### Objective
Develop a program to model a flow network for goods logistics from terminals through warehouses to retail stores using the maximum flow algorithm. Perform an analysis of the obtained results and compare them with theoretical expectations.

### Task Description
You are to construct a graph model representing the flow network based on the following structure and data.

### Graph Structure
The graph consists of nodes representing Terminals, Warehouses, and Stores, with edges indicating the capacity (maximum amount of goods that can be transferred).

Edge Capacities
From	To	Capacity (units)
Terminal 1	Warehouse 1	25
Terminal 1	Warehouse 2	20
Terminal 1	Warehouse 3	15
Terminal 2	Warehouse 3	15
Terminal 2	Warehouse 4	30
Terminal 2	Warehouse 2	10
Warehouse 1	Store 1	15
Warehouse 1	Store 2	10
Warehouse 1	Store 3	20
Warehouse 2	Store 4	15
Warehouse 2	Store 5	10
Warehouse 2	Store 6	25
Warehouse 3	Store 7	20
Warehouse 3	Store 8	15
Warehouse 3	Store 9	10
Warehouse 4	Store 10	20
Warehouse 4	Store 11	10
Warehouse 4	Store 12	15
Warehouse 4	Store 13	5
Warehouse 4	Store 14	10

### Technical Requirements
Use the Edmonds-Karp algorithm (an implementation of Ford-Fulkerson) to calculate the maximum flow.

The graph should include 20 vertices and use the given edge capacities.
