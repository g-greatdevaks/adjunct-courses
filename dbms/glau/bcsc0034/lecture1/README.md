# Lecture 1: Python Connectivity & Database Design Principles

This directory contains the core materials for Lecture 1 of the Database Management Systems (DBMS) module at GLA University.

## Overview

This lecture establishes the dual foundations of modern database interactions: programmatic connectivity and relational structural integrity. It traverses from raw, un-sanitized flat datasets to highly optimized, normalized relational schemas.

### Key Learnings and Coverage:

- **Python DB-API Connectivity**: Programmatic communication using `mysql.connector` contextual managers.
- **Security & Sanitization**: Utilizing bind parameters (`%s` placeholders) to neutralize SQL Injection vulnerabilities.
- **High-Performance Batch Ingestion**: Optimizing data migration using `executemany()` server-side batching versus row-by-row overhead.
- **Structural Normalization Progression**:
  - **1NF to 3NF**: Traditional normalization resolving partial and transitive dependencies.
  - **BCNF (Boyce-Codd Normal Form)**: Handling anomalies where determinant attributes are not candidate keys.
  - **4NF & 5NF (Theoretical Overview)**: Multi-valued and Join dependencies.
  - **6NF (Temporal Schema)**: Complete decomposition for time-series analytics and audit-history tracking.
- **Anomalies & Edge Evaluations**: Physical observations of Insertion, Update, and Deletion anomalies, alongside Lossy-Join interpretations (Spurious Rows).
- **Interactive Verifications & Schema Visuals**: Rendering Entity-Relationship Diagrams (ERDs) via zero-dependency web hooks (Mermaid.js APIs).
- **Strategic De-Normalization**: Evaluating trade-offs contrasting OLTP write optimization with OLAP read-heavy dashboard caches.

## Contents

- **`dbms_foundations.ipynb`**: Interactive Jupyter Notebook containing both lecture explanations and hands-on laboratory exercises.
- **`assets/`**: Repository of flat CSV datasets simulation real-world transactional loads.
- **`lab_cheatsheet/`**: Interactive CLI support tools for validating Lab 1.
