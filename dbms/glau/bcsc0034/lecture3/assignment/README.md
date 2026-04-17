# Take-Home Assignment: Multi-Store Analytics System - Part 2

## Objective

This assignment evaluates the understanding of query optimization and execution plan analysis (Lecture 3). It continues from the scenario established in Lecture 2's assignment.

## Prerequisites

This assignment assumes you have already completed Task 1 and Task 2 of the Lecture 2 assignment, and have the `retail_db` (or `ecommerce_db`) database set up with populated data.

## Tasks

### Task 1: Query Optimization and Analysis

1.  **The Bottleneck**: Write a query to find the total quantity sold for a specific product in a specific store within a specific date range.
2.  **Analysis**: Run `EXPLAIN` on this query and observe the execution plan. Note the `type` and `rows` columns.
3.  **Optimization**: Create a composite index on the `sales` table to optimize this query. Determine the best order of columns for the index based on the Leftmost Prefix Rule.
4.  **Verification**: Re-run `EXPLAIN` and verify that the execution plan now utilizes the index instead of a full table scan.
