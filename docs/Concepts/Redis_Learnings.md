# Redis
---

## Redis Fundamentals

- [ ] 🔷 What is Redis?
- [ ] 🔷 Redis Architecture
- [ ] 🔷 In-Memory Database
- [ ] 🔷 Redis Use Cases
- [ ] 🔷 Redis vs Memcached
- [ ] 🔷 Redis vs PostgreSQL
- [ ] 🔷 Redis Data Model
- [ ] 🔷 Redis Persistence Overview
- [ ] 🟣 Redis Internals

---

## Installation & Setup

- [ ] 🔷 Installing Redis
- [ ] 🔷 Redis Server
- [ ] 🔷 Redis CLI
- [ ] 🔷 Configuration File (redis.conf)
- [ ] 🔷 Connecting to Redis
- [ ] 🔷 Docker Setup
- [ ] 🔷 Docker Compose Setup
- [ ] 🔷 Environment Variables
- [ ] 🟣 Redis Sentinel Setup

---

## Redis Data Types

- [ ] 🔷 Strings
- [ ] 🔷 Lists
- [ ] 🔷 Sets
- [ ] 🔷 Sorted Sets (ZSET)
- [ ] 🔷 Hashes
- [ ] 🔷 Bitmaps
- [ ] 🔷 HyperLogLog
- [ ] 🔷 Streams
- [ ] 🟣 Geospatial Indexes

---

## String Operations

- [ ] 🔷 SET
- [ ] 🔷 GET
- [ ] 🔷 MSET
- [ ] 🔷 MGET
- [ ] 🔷 SETEX
- [ ] 🔷 GETSET
- [ ] 🔷 APPEND
- [ ] 🔷 INCR
- [ ] 🔷 DECR
- [ ] 🔷 INCRBY
- [ ] 🔷 DECRBY
- [ ] 🔷 GETRANGE
- [ ] 🔷 SETRANGE

---

## Hash Operations

- [ ] 🔷 HSET
- [ ] 🔷 HGET
- [ ] 🔷 HMSET
- [ ] 🔷 HMGET
- [ ] 🔷 HGETALL
- [ ] 🔷 HDEL
- [ ] 🔷 HEXISTS
- [ ] 🔷 HKEYS
- [ ] 🔷 HVALS
- [ ] 🔷 HLEN

---

## List Operations

- [ ] 🔷 LPUSH
- [ ] 🔷 RPUSH
- [ ] 🔷 LPOP
- [ ] 🔷 RPOP
- [ ] 🔷 LRANGE
- [ ] 🔷 LLEN
- [ ] 🔷 LINDEX
- [ ] 🔷 LSET
- [ ] 🔷 LTRIM
- [ ] 🔷 BLPOP
- [ ] 🔷 BRPOP

---

## Set Operations

- [ ] 🔷 SADD
- [ ] 🔷 SREM
- [ ] 🔷 SMEMBERS
- [ ] 🔷 SISMEMBER
- [ ] 🔷 SCARD
- [ ] 🔷 SUNION
- [ ] 🔷 SINTER
- [ ] 🔷 SDIFF
- [ ] 🔷 SPOP

---

## Sorted Set Operations

- [ ] 🔷 ZADD
- [ ] 🔷 ZREM
- [ ] 🔷 ZRANGE
- [ ] 🔷 ZREVRANGE
- [ ] 🔷 ZSCORE
- [ ] 🔷 ZRANK
- [ ] 🔷 ZREVRANK
- [ ] 🔷 ZCOUNT
- [ ] 🔷 ZCARD

---

## Key Management

- [ ] 🔷 DEL
- [ ] 🔷 EXISTS
- [ ] 🔷 EXPIRE
- [ ] 🔷 TTL
- [ ] 🔷 PERSIST
- [ ] 🔷 RENAME
- [ ] 🔷 KEYS
- [ ] 🔷 SCAN
- [ ] 🔷 TYPE
- [ ] 🔷 RANDOMKEY
- [ ] 🟣 UNLINK

---

## Expiration & TTL

- [ ] 🔷 EXPIRE
- [ ] 🔷 PEXPIRE
- [ ] 🔷 TTL
- [ ] 🔷 PTTL
- [ ] 🔷 EXPIREAT
- [ ] 🔷 Cache Expiration Strategies
- [ ] 🟣 Lazy Expiration
- [ ] 🟣 Active Expiration

---

## Persistence

- [ ] 🔷 RDB Snapshots
- [ ] 🔷 AOF (Append Only File)
- [ ] 🔷 RDB vs AOF
- [ ] 🔷 Backup
- [ ] 🔷 Restore
- [ ] 🟣 AOF Rewrite

---

## Transactions

- [ ] 🔷 MULTI
- [ ] 🔷 EXEC
- [ ] 🔷 DISCARD
- [ ] 🔷 WATCH
- [ ] 🔷 Optimistic Locking
- [ ] 🟣 Lua Transactions

---

## Pub/Sub

- [ ] 🔷 PUBLISH
- [ ] 🔷 SUBSCRIBE
- [ ] 🔷 PSUBSCRIBE
- [ ] 🔷 Channel Messaging
- [ ] 🔷 Pattern Subscription
- [ ] 🟣 Cluster Pub/Sub

---

## Redis Streams

- [ ] 🔷 XADD
- [ ] 🔷 XRANGE
- [ ] 🔷 XREAD
- [ ] 🔷 Consumer Groups
- [ ] 🔷 Message Processing
- [ ] 🟣 Stream Trimming

---

## Caching

- [ ] 🔷 Cache Basics
- [ ] 🔷 Cache Aside Pattern
- [ ] 🔷 Read Through Cache
- [ ] 🔷 Write Through Cache
- [ ] 🔷 Write Back Cache
- [ ] 🔷 Cache Invalidation
- [ ] 🔷 Cache Warming
- [ ] 🔷 Cache Eviction
- [ ] 🟣 Refresh Ahead Cache

---

## Eviction Policies

- [ ] 🔷 noeviction
- [ ] 🔷 allkeys-lru
- [ ] 🔷 volatile-lru
- [ ] 🔷 allkeys-random
- [ ] 🔷 volatile-random
- [ ] 🔷 volatile-ttl
- [ ] 🔷 allkeys-lfu
- [ ] 🟣 volatile-lfu

---

## Distributed Locking

- [ ] 🔷 SET NX EX
- [ ] 🔷 Lock Expiration
- [ ] 🔷 Lock Release
- [ ] 🟣 Redlock Algorithm

---

## Redis with Python

- [ ] 🔷 redis-py
- [ ] 🔷 Connecting to Redis
- [ ] 🔷 CRUD Operations
- [ ] 🔷 Pipelines
- [ ] 🔷 Transactions
- [ ] 🔷 Pub/Sub
- [ ] 🔷 Connection Pooling
- [ ] 🔷 Async Redis
- [ ] 🟣 aioredis Internals

---

## Redis with Django

- [ ] 🔷 django-redis
- [ ] 🔷 Cache Backend
- [ ] 🔷 Session Storage
- [ ] 🔷 Cache Configuration
- [ ] 🔷 View Caching
- [ ] 🟣 Fragment Caching

---

## Redis with FastAPI

- [ ] 🔷 Redis Dependency
- [ ] 🔷 Connection Management
- [ ] 🔷 Async Redis
- [ ] 🔷 Response Caching
- [ ] 🔷 Rate Limiting
- [ ] 🔷 Background Tasks
- [ ] 🟣 Distributed Locks

---

## Celery Integration

- [ ] 🔷 Redis as Broker
- [ ] 🔷 Redis as Result Backend
- [ ] 🔷 Task Queue
- [ ] 🔷 Delayed Tasks
- [ ] 🔷 Retry Mechanism
- [ ] 🟣 Task Scheduling

---

## Performance Optimization

- [ ] 🔷 Pipelining
- [ ] 🔷 Connection Pooling
- [ ] 🔷 Batch Operations
- [ ] 🔷 Avoid Large Keys
- [ ] 🔷 Key Naming Strategy
- [ ] 🔷 Memory Optimization
- [ ] 🔷 Hot Keys
- [ ] 🟣 Lua Scripting Optimization

---

## Monitoring

- [ ] 🔷 INFO
- [ ] 🔷 MONITOR
- [ ] 🔷 SLOWLOG
- [ ] 🔷 MEMORY Command
- [ ] 🔷 CLIENT LIST
- [ ] 🔷 Latency Monitoring
- [ ] 🟣 Redis Insight

---

## Security

- [ ] 🔷 AUTH
- [ ] 🔷 ACL
- [ ] 🔷 Password Protection
- [ ] 🔷 Protected Mode
- [ ] 🔷 TLS
- [ ] 🔷 Network Security
- [ ] 🟣 Command Renaming

---

## Replication & High Availability

- [ ] 🔷 Master-Replica Replication
- [ ] 🔷 Read Replicas
- [ ] 🔷 Replication Lag
- [ ] 🟣 Redis Sentinel
- [ ] 🟣 Redis Cluster
- [ ] 🟣 Automatic Failover

---

## Memory Management

- [ ] 🔷 maxmemory
- [ ] 🔷 Memory Usage
- [ ] 🔷 Memory Fragmentation
- [ ] 🔷 Eviction Policies
- [ ] 🔷 Object Encoding
- [ ] 🟣 Active Defragmentation

---

## Redis Best Practices

- [ ] 🔷 Key Naming Convention
- [ ] 🔷 TTL Strategy
- [ ] 🔷 Avoid KEYS in Production
- [ ] 🔷 Prefer SCAN
- [ ] 🔷 Proper Serialization
- [ ] 🔷 Connection Pooling
- [ ] 🔷 Cache Invalidation Strategy
- [ ] 🔷 Monitor Memory Usage
- [ ] 🔷 Avoid Large Values
- [ ] 🟣 Sharding Strategy

---

## Redis Interview Questions

- [ ] 🔷 Redis vs Memcached
- [ ] 🔷 Redis vs Database
- [ ] 🔷 Why Redis is Fast
- [ ] 🔷 Strings vs Hashes
- [ ] 🔷 Pub/Sub vs Streams
- [ ] 🔷 RDB vs AOF
- [ ] 🔷 Cache Aside Pattern
- [ ] 🔷 Cache Stampede
- [ ] 🔷 Cache Penetration
- [ ] 🔷 Cache Avalanche
- [ ] 🔷 Cache Breakdown
- [ ] 🔷 TTL
- [ ] 🔷 Pipelining
- [ ] 🔷 Connection Pooling
- [ ] 🔷 Distributed Locking
- [ ] 🔷 Redis Transactions
- [ ] 🟣 Redis Cluster
- [ ] 🟣 Redis Sentinel
- [ ] 🟣 Redlock Algorithm
- [ ] 🟣 Lua Scripting
