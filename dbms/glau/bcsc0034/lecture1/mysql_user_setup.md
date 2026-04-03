# MySQL / MariaDB User Management Cheat Sheet

This document provides utility commands for creating and managing users in MySQL/MariaDB, particularly useful for setting up laboratory environments.

## Connecting as Root

Before creating users, connecting as an administrator (root) is required.

```bash
# On Linux (often uses system socket auth, no password needed if using sudo)
sudo mysql

# Or standard connection (prompting for root password)
mysql -u root -p
```

## User Creation

Users are defined by `Username@Host`. The host designates from where the connection is allowed to originate.

### 1. Local-Only User (Recommended for Labs)

The user can only connect if the client is running on the same machine as the server.

```sql
CREATE USER 'student'@'localhost' IDENTIFIED BY 'dummy_password';
```

### 2. Remote-Accessible User

The `%` is a wildcard meaning "any host". This option is utilized when connecting from a remote machine or container without network isolation.

```sql
CREATE USER 'student'@'%' IDENTIFIED BY 'dummy_password';
```

## Granting Privileges

Privileges define what the user is allowed to do.

### 1. Granting Full Access to a Specific Database

This is the preferred approach for local setups to keep environments isolated.

```sql
-- Grant all permissions on 'student_tasks' database and all its tables
GRANT ALL PRIVILEGES ON student_tasks.* TO 'student'@'localhost';
```

### 2. Reloading Privileges

Running this command after a `GRANT` ensures that the server applies the changes immediately.

```sql
FLUSH PRIVILEGES;
```

## Verifying Configurations

### 1. View Existing Users in System

```sql
USE mysql;
SELECT User, Host FROM user;
```

## Removing Users

```sql
DROP USER 'student'@'localhost';
```
