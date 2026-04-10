# Take-Home Assignment: Multi-Store Analytics System

## Objective

This assignment evaluates the combined understanding of database design principles (Lecture 1) and advanced data retrieval and optimization techniques (Lecture 2). Students will step into the role of a data engineer building a reporting system for a retail chain with multiple physical stores.

## Scenario

A retail chain operates multiple stores. The management requires a centralized reporting system to analyze sales performance, manage inventory, and identify optimization opportunities.

## Tasks

### Task 1: Database Schema Design (Lecture 1)

Design a normalized relational schema to support the multi-store operations. The schema must include the following tables:

1.  **`stores`**: `id`, `location`.
2.  **`products`**: `id`, `name`, `price`.
3.  **`inventory`**: `store_id`, `product_id`, `stock_quantity`.
4.  **`sales`**: `id`, `store_id`, `product_id`, `quantity`, `sale_date`.

**Requirements**:

- Create the tables in the `ecommerce_db` database (or a new database named `retail_db`).
- Ensure all Foreign Key, Primary Key, and Composite Key constraints are explicitly defined.
- Choose appropriate data types for all columns.

### Task 2: Data Ingestion (Lecture 1)

Write a Python script utilizing `mysql.connector` to populate the tables with mock data.

- Generate at least 5 stores.
- Generate at least 50 products.
- Populate inventory for each store.
- Generate at least 5,000 sales records distributed across stores and products.
- _Tip_: Utilize batch insertion (`executemany()`) for performance, as taught in Lecture 1.

### Task 3: Advanced Data Retrieval (Lecture 2)

Write Python functions to execute the following queries using SQL:

1.  **High-Performing Stores**: Find stores whose total sales revenue is greater than the average total sales revenue across all stores. (Hint: Requires a subquery in the `HAVING` clause).
2.  **Localized Dead Stock**: Identify products that are in stock in a specific store (inventory > 0) but have never been sold in that specific store. (Hint: Requires a subquery with `NOT IN` or `NOT EXISTS`).

### Task 4: Query Optimization and Analysis (Lecture 2)

1.  **The Bottleneck**: Write a query to find the total quantity sold for a specific product in a specific store within a specific date range.
2.  **Analysis**: Run `EXPLAIN` on this query and observe the execution plan. Note the `type` and `rows` columns.
3.  **Optimization**: Create a composite index on the `sales` table to optimize this query. Determine the best order of columns for the index based on the Leftmost Prefix Rule.
4.  **Verification**: Re-run `EXPLAIN` and verify that the execution plan now utilizes the index instead of a full table scan.
