# SQLAlchemy
---

## SQLAlchemy Fundamentals

- [ ] 🔷 What is SQLAlchemy?
- [ ] 🔷 SQLAlchemy Architecture
- [ ] 🔷 ORM vs Core
- [ ] 🔷 SQLAlchemy Components
- [ ] 🔷 SQLAlchemy 2.0 Overview
- [ ] 🔷 SQLAlchemy with FastAPI
- [ ] 🔷 SQLAlchemy with Flask
- [ ] 🔷 SQLAlchemy with PostgreSQL
- [ ] 🟣 SQLAlchemy Internals

---

## Installation & Setup

- [ ] 🔷 Installing SQLAlchemy
- [ ] 🔷 Installing Database Drivers
- [ ] 🔷 Project Structure
- [ ] 🔷 Database URL
- [ ] 🔷 Engine Creation
- [ ] 🔷 Environment Variables
- [ ] 🔷 Configuration Management
- [ ] 🟣 Multiple Database Configuration

---

## Engine

- [ ] 🔷 create_engine()
- [ ] 🔷 Engine Object
- [ ] 🔷 Database URL
- [ ] 🔷 Echo Mode
- [ ] 🔷 Pool Configuration
- [ ] 🔷 Engine Disposal
- [ ] 🟣 Async Engine

---

## Connection Management

- [ ] 🔷 Connection Object
- [ ] 🔷 Opening Connections
- [ ] 🔷 Closing Connections
- [ ] 🔷 Context Managers
- [ ] 🔷 Connection Pooling
- [ ] 🟣 Connection Events

---

## Declarative ORM

- [ ] 🔷 Declarative Base
- [ ] 🔷 Base Class
- [ ] 🔷 Declarative Models
- [ ] 🔷 __tablename__
- [ ] 🔷 Metadata
- [ ] 🔷 Table Mapping
- [ ] 🟣 Declarative Mixins

---

## Models

- [ ] 🔷 Column
- [ ] 🔷 Primary Key
- [ ] 🔷 Foreign Key
- [ ] 🔷 Nullable
- [ ] 🔷 Default Values
- [ ] 🔷 Unique Constraint
- [ ] 🔷 Check Constraint
- [ ] 🔷 Composite Keys
- [ ] 🟣 Composite Mappings

---

## SQLAlchemy Data Types

- [ ] 🔷 Integer
- [ ] 🔷 String
- [ ] 🔷 Text
- [ ] 🔷 Boolean
- [ ] 🔷 Float
- [ ] 🔷 Numeric
- [ ] 🔷 Date
- [ ] 🔷 DateTime
- [ ] 🔷 Time
- [ ] 🔷 UUID
- [ ] 🔷 JSON
- [ ] 🔷 JSONB
- [ ] 🔷 Enum
- [ ] 🟣 Custom Types

---

## Sessions

- [ ] 🔷 Session
- [ ] 🔷 SessionLocal
- [ ] 🔷 Session Lifecycle
- [ ] 🔷 Commit
- [ ] 🔷 Rollback
- [ ] 🔷 Flush
- [ ] 🔷 Refresh
- [ ] 🔷 Expire
- [ ] 🔷 Close Session
- [ ] 🟣 Scoped Session

---

## CRUD Operations

- [ ] 🔷 Insert
- [ ] 🔷 Select
- [ ] 🔷 Update
- [ ] 🔷 Delete
- [ ] 🔷 Bulk Insert
- [ ] 🔷 Bulk Update
- [ ] 🔷 Bulk Delete
- [ ] 🟣 Bulk Operations Performance

---

## Querying

- [ ] 🔷 select()
- [ ] 🔷 where()
- [ ] 🔷 filter()
- [ ] 🔷 filter_by()
- [ ] 🔷 order_by()
- [ ] 🔷 group_by()
- [ ] 🔷 having()
- [ ] 🔷 limit()
- [ ] 🔷 offset()
- [ ] 🔷 distinct()
- [ ] 🔷 scalar()
- [ ] 🔷 first()
- [ ] 🔷 one()
- [ ] 🔷 all()
- [ ] 🟣 selectinload() Optimization

---

## Relationships

- [ ] 🔷 relationship()
- [ ] 🔷 One-to-One
- [ ] 🔷 One-to-Many
- [ ] 🔷 Many-to-One
- [ ] 🔷 Many-to-Many
- [ ] 🔷 back_populates
- [ ] 🔷 backref
- [ ] 🔷 cascade
- [ ] 🔷 lazy Loading
- [ ] 🟣 Association Objects

---

## Relationship Loading

- [ ] 🔷 Lazy Loading
- [ ] 🔷 Joined Loading
- [ ] 🔷 selectinload()
- [ ] 🔷 subqueryload()
- [ ] 🔷 joinedload()
- [ ] 🔷 contains_eager()
- [ ] 🟣 raiseload()

---

## Joins

- [ ] 🔷 join()
- [ ] 🔷 outerjoin()
- [ ] 🔷 Multiple Joins
- [ ] 🔷 Self Join
- [ ] 🔷 Aliases
- [ ] 🟣 Complex Join Expressions

---

## Filtering

- [ ] 🔷 AND
- [ ] 🔷 OR
- [ ] 🔷 NOT
- [ ] 🔷 IN
- [ ] 🔷 BETWEEN
- [ ] 🔷 LIKE
- [ ] 🔷 ILIKE
- [ ] 🔷 EXISTS
- [ ] 🟣 Hybrid Filters

---

## Aggregations

- [ ] 🔷 func.count()
- [ ] 🔷 func.sum()
- [ ] 🔷 func.avg()
- [ ] 🔷 func.min()
- [ ] 🔷 func.max()
- [ ] 🔷 GROUP BY
- [ ] 🔷 HAVING
- [ ] 🟣 Window Functions

---

## Transactions

- [ ] 🔷 Transaction Management
- [ ] 🔷 Commit
- [ ] 🔷 Rollback
- [ ] 🔷 Nested Transactions
- [ ] 🔷 Savepoints
- [ ] 🟣 Two Phase Commit

---

## Async SQLAlchemy

- [ ] 🔷 Async Engine
- [ ] 🔷 Async Session
- [ ] 🔷 Async CRUD
- [ ] 🔷 Async Queries
- [ ] 🔷 Async Transactions
- [ ] 🔷 asyncpg
- [ ] 🟣 Async Connection Pool

---

## SQL Expressions (Core)

- [ ] 🔷 select()
- [ ] 🔷 insert()
- [ ] 🔷 update()
- [ ] 🔷 delete()
- [ ] 🔷 text()
- [ ] 🔷 bindparam()
- [ ] 🔷 func
- [ ] 🔷 case()
- [ ] 🟣 Custom SQL Expressions

---

## Raw SQL

- [ ] 🔷 text()
- [ ] 🔷 execute()
- [ ] 🔷 Parameterized Queries
- [ ] 🔷 SQL Injection Prevention
- [ ] 🟣 Stored Procedure Calls

---

## Constraints

- [ ] 🔷 Primary Key
- [ ] 🔷 Foreign Key
- [ ] 🔷 Unique
- [ ] 🔷 Check
- [ ] 🔷 Index
- [ ] 🟣 Composite Constraints

---

## Indexes

- [ ] 🔷 Single Index
- [ ] 🔷 Composite Index
- [ ] 🔷 Unique Index
- [ ] 🔷 Index Performance
- [ ] 🟣 Partial Indexes

---

## Migrations

- [ ] 🔷 Alembic
- [ ] 🔷 Migration Environment
- [ ] 🔷 Revision
- [ ] 🔷 Upgrade
- [ ] 🔷 Downgrade
- [ ] 🔷 Autogenerate
- [ ] 🔷 Data Migrations
- [ ] 🟣 Branch Migrations

---

## Performance Optimization

- [ ] 🔷 Query Optimization
- [ ] 🔷 Avoid N+1 Queries
- [ ] 🔷 joinedload()
- [ ] 🔷 selectinload()
- [ ] 🔷 Bulk Operations
- [ ] 🔷 Pagination
- [ ] 🔷 Connection Pooling
- [ ] 🔷 Query Profiling
- [ ] 🟣 Compiled Queries

---

## Events

- [ ] 🔷 ORM Events
- [ ] 🔷 Session Events
- [ ] 🔷 Mapper Events
- [ ] 🔷 Connection Events
- [ ] 🟣 Custom Event Listeners

---

## Hybrid Properties

- [ ] 🔷 @hybrid_property
- [ ] 🔷 Hybrid Methods
- [ ] 🔷 Computed Fields
- [ ] 🟣 Advanced Hybrid Expressions

---

## Security

- [ ] 🔷 Parameterized Queries
- [ ] 🔷 SQL Injection Prevention
- [ ] 🔷 Environment Variables
- [ ] 🔷 Secure Credentials
- [ ] 🟣 Database Encryption

---

## Testing

- [ ] 🔷 Unit Testing
- [ ] 🔷 pytest
- [ ] 🔷 In-Memory SQLite
- [ ] 🔷 Test Database
- [ ] 🔷 Fixtures
- [ ] 🔷 Mock Sessions
- [ ] 🟣 Transaction Rollback Testing

---

## SQLAlchemy with FastAPI

- [ ] 🔷 Dependency Injection
- [ ] 🔷 Session Dependency
- [ ] 🔷 CRUD Repository
- [ ] 🔷 Response Models
- [ ] 🔷 Pagination
- [ ] 🔷 Error Handling
- [ ] 🔷 Async Integration
- [ ] 🟣 Generic Repository Pattern

---

## SQLAlchemy with Django

- [ ] 🟣 SQLAlchemy alongside Django
- [ ] 🟣 Django + SQLAlchemy Integration

---

## Best Practices

- [ ] 🔷 Repository Pattern
- [ ] 🔷 Service Layer
- [ ] 🔷 Session Per Request
- [ ] 🔷 Transaction Management
- [ ] 🔷 Keep Business Logic Outside Models
- [ ] 🔷 Proper Relationship Loading
- [ ] 🔷 Efficient Queries
- [ ] 🔷 Clean Project Structure
- [ ] 🟣 Unit of Work Pattern
- [ ] 🟣 Domain Driven Design (DDD)

---

## SQLAlchemy Interview Questions

- [ ] 🔷 ORM vs Raw SQL
- [ ] 🔷 ORM vs SQLAlchemy Core
- [ ] 🔷 Session vs Engine
- [ ] 🔷 Commit vs Flush
- [ ] 🔷 Flush vs Refresh
- [ ] 🔷 Lazy Loading vs Eager Loading
- [ ] 🔷 joinedload() vs selectinload()
- [ ] 🔷 Relationship Types
- [ ] 🔷 Connection Pooling
- [ ] 🔷 Alembic
- [ ] 🔷 Async SQLAlchemy
- [ ] 🔷 SQL Injection Prevention
- [ ] 🔷 Transaction Management
- [ ] 🔷 Repository Pattern
- [ ] 🟣 Identity Map
- [ ] 🟣 Unit of Work
- [ ] 🟣 SQLAlchemy Internals
