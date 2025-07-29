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


## Task 2: Comparing the Efficiency of OOBTree and dict for Range Queries
### Objective
Develop a program to store a large dataset of products in two data structures — OOBTree and dict — and perform a comparative analysis of their performance when executing range queries.

### Task Description
Use the provided file generated_items_data.csv to load product information. Each product includes a unique ID, Name, Category, and Price.

Implement two storage structures for the products:

The first is OOBTree from the BTrees library, where the key is the product ID and the value is a dictionary with the product’s attributes.

The second is the built-in Python dict, using the same structure.

Create the following functions to add products to each structure:

- add_item_to_tree

- add_item_to_dict

Create functions to perform range queries, retrieving all products within a specified price range:

- range_query_tree

- range_query_dict

Measure the total execution time of the range query for each structure using the timeit module.

Run each range query function 100 times to calculate the average execution time.

Output the total execution time for each structure, including how long it takes to run 100 range queries for both OOBTree and dict.

### Technical Requirements
Use only OOBTree and the built-in dict for the comparison.

Implement separate functions for adding items:

- add_item_to_tree

- add_item_to_dict

Implement separate functions for range queries:

- range_query_tree

- range_query_dict

Use the timeit module to measure performance accurately.

Time measurement must be based on 100 range queries per structure.