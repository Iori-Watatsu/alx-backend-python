# ALX Backend Python Projects

This repository contains Python projects and exercises focused on **decorators, context managers, asynchronous programming, and unit testing**, part of the ALX Backend curriculum.

## Table of Contents

- [Project Structure](#project-structure)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage Examples](#usage-examples)
- [Running Tests](#running-tests)

## Project Structure

alx-backend-python/
│
├─ python-decorators-0x01/
│ ├─ 0-log_queries.py
│ ├─ 1-with_db_connection.py
│ ├─ 2-transactional.py
│ ├─ 3-retry_on_failure.py
│ └─ 4-cache_query.py
│
├─ python-context-async-perations-0x02/
│ ├─ 0-databaseconnection.py
│ ├─ 1-execute.py
│ ├─ 2-custom_contexts.py
│ └─ 3-concurrent.py
│
├─ 0x03-Unittests_and_integration_tests/
│ └─ test_utils.py
│
└─ README.md


## Features

### Decorators
- **`log_queries`**: Logs SQL queries with timestamps.
- **`with_db_connection`**: Automatically opens and closes database connections.
- **`transactional`**: Wraps DB operations in a transaction (commit/rollback).
- **`retry_on_failure`**: Retries DB operations on transient failures.
- **`cache_query`**: Caches SQL query results to avoid redundant calls.

### Context Managers
- **`DatabaseConnection`**: Class-based context manager for DB connections.
- **`ExecuteQuery`**: Executes queries inside a reusable context manager.

### Async Database Operations
- Uses `aiosqlite` and `asyncio.gather` to run multiple queries concurrently.

### Unit Tests
- Tests functions like `access_nested_map` with **parameterized inputs**.

## Getting Started

1. **Clone the repository**
```bash
git clone https://github.com/<your-username>/alx-backend-python.git
cd alx-backend-python

