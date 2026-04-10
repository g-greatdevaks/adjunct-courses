# Lecture 2: Advanced Data Retrieval & Subqueries

This directory contains the core materials for Lecture 2 of the Database Management Systems (DBMS) module.

## Overview

This lecture delves into advanced data retrieval techniques. It covers the execution order of SQL statements, subqueries, and the relevance of threading and concurrency in database systems.

### Key Learnings and Coverage:

- **Lecture 1 Recap**: Key highlights and supplemental details regarding normalization and connectivity.
- **Threading and Concurrency in Databases**: The relationship between threads, concurrency, parallelism, and database connections/pooling.
- **Execution Order of SQL Statements**: The mechanics of how database engines interpret and process queries.
- **Subqueries (Nested Queries)**: Introduction to using subqueries in WHERE, FROM, and SELECT clauses.

## Contents

- **`dbms_advanced_queries.ipynb`**: Interactive Jupyter Notebook containing lecture explanations and hands-on laboratory exercises.
- **`assignment/`**: Directory containing the take-home assignment instructions.

## Prerequisites and Environment Setup

To execute the exercises in the notebook, follow the instructions below based on the operating system.

### 1. Virtual Environment Configuration

**On Linux / macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Installing the Jupyter Kernel

To ensure the notebook uses the dependencies installed in the virtual environment:

1. Install `ipykernel` inside the activated virtual environment:

```bash
python -m pip install ipykernel
```

2. Register the kernel:

```bash
python -m ipykernel install --user --name=dbms-lecture2 --display-name "Python (DBMS Lecture 2)"
```

3. In the Jupyter Notebook interface, navigate to the menu: **Kernel** -> **Change Kernel** and select **Python (DBMS Lecture 2)**.

### 3. Dependencies

Install the required packages:

```bash
python -m pip install mysql-connector-python Faker
```

> [!NOTE]
> Utilizing `python -m pip` instead of the bare `pip` command ensures that the packages are installed for the specific Python interpreter currently active or targeted, avoiding conflicts when multiple Python installations exist on the system.
