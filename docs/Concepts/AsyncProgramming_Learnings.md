# Async Programming
---

## Async Programming Fundamentals

- [ ] 🔷 What is Asynchronous Programming?
- [ ] 🔷 Synchronous vs Asynchronous
- [ ] 🔷 Concurrency vs Parallelism
- [ ] 🔷 Blocking vs Non-Blocking
- [ ] 🔷 I/O Bound vs CPU Bound
- [ ] 🔷 Event-Driven Programming
- [ ] 🔷 Cooperative Multitasking
- [ ] 🟣 Reactive Programming

---

## Python Async Basics

- [ ] 🔷 async Keyword
- [ ] 🔷 await Keyword
- [ ] 🔷 Coroutine
- [ ] 🔷 Coroutine Function
- [ ] 🔷 Coroutine Object
- [ ] 🔷 Event Loop
- [ ] 🔷 asyncio Module
- [ ] 🔷 Running Coroutines
- [ ] 🟣 Coroutine Internals

---

## Event Loop

- [ ] 🔷 What is Event Loop?
- [ ] 🔷 asyncio.run()
- [ ] 🔷 get_running_loop()
- [ ] 🔷 Loop Lifecycle
- [ ] 🔷 Scheduling Tasks
- [ ] 🔷 Stopping Event Loop
- [ ] 🔷 Closing Event Loop
- [ ] 🟣 Custom Event Loop

---

## Tasks

- [ ] 🔷 asyncio.create_task()
- [ ] 🔷 Task Lifecycle
- [ ] 🔷 Running Multiple Tasks
- [ ] 🔷 Task Cancellation
- [ ] 🔷 Task Status
- [ ] 🔷 Task Naming
- [ ] 🔷 Awaiting Tasks
- [ ] 🟣 Task Groups

---

## Gathering Tasks

- [ ] 🔷 asyncio.gather()
- [ ] 🔷 Concurrent Execution
- [ ] 🔷 return_exceptions
- [ ] 🔷 Nested gather()
- [ ] 🟣 asyncio.wait()

---

## Sleeping & Timing

- [ ] 🔷 asyncio.sleep()
- [ ] 🔷 Non-Blocking Sleep
- [ ] 🔷 Timeout Basics
- [ ] 🔷 asyncio.timeout()
- [ ] 🔷 asyncio.wait_for()
- [ ] 🟣 Scheduling Delayed Tasks

---

## Async Context Managers

- [ ] 🔷 async with
- [ ] 🔷 __aenter__
- [ ] 🔷 __aexit__
- [ ] 🔷 Resource Management
- [ ] 🟣 Custom Async Context Managers

---

## Async Iteration

- [ ] 🔷 async for
- [ ] 🔷 Async Iterators
- [ ] 🔷 Async Generators
- [ ] 🔷 yield
- [ ] 🔷 Async Streaming
- [ ] 🟣 Custom Async Iterables

---

## Synchronization

- [ ] 🔷 asyncio.Lock
- [ ] 🔷 asyncio.Event
- [ ] 🔷 asyncio.Semaphore
- [ ] 🔷 asyncio.Queue
- [ ] 🔷 Producer Consumer Pattern
- [ ] 🟣 asyncio.Condition
- [ ] 🟣 asyncio.Barrier

---

## Exception Handling

- [ ] 🔷 try/except in Async Code
- [ ] 🔷 Exception Propagation
- [ ] 🔷 Handling CancelledError
- [ ] 🔷 TimeoutError
- [ ] 🔷 gather() Exception Handling
- [ ] 🟣 Exception Groups

---

## Threading Integration

- [ ] 🔷 Threading vs Asyncio
- [ ] 🔷 asyncio.to_thread()
- [ ] 🔷 run_in_executor()
- [ ] 🔷 ThreadPoolExecutor
- [ ] 🔷 Mixing Threads & Async
- [ ] 🟣 ProcessPoolExecutor

---

## Multiprocessing

- [ ] 🔷 Multiprocessing vs Asyncio
- [ ] 🔷 CPU Bound Tasks
- [ ] 🔷 ProcessPoolExecutor
- [ ] 🔷 Offloading Heavy Tasks
- [ ] 🟣 Shared Memory

---

## Async File Operations

- [ ] 🔷 aiofiles
- [ ] 🔷 Reading Files
- [ ] 🔷 Writing Files
- [ ] 🔷 Async File Streaming
- [ ] 🟣 Memory Mapped Files

---

## Async HTTP

- [ ] 🔷 httpx AsyncClient
- [ ] 🔷 aiohttp
- [ ] 🔷 Async GET Requests
- [ ] 🔷 Async POST Requests
- [ ] 🔷 Connection Pooling
- [ ] 🔷 Request Timeouts
- [ ] 🔷 Retry Logic
- [ ] 🟣 HTTP Streaming

---

## Async Database

- [ ] 🔷 Async SQLAlchemy
- [ ] 🔷 Async Session
- [ ] 🔷 Async Engine
- [ ] 🔷 Async Transactions
- [ ] 🔷 asyncpg
- [ ] 🔷 Connection Pooling
- [ ] 🟣 Database Connection Tuning

---

## Async Redis

- [ ] 🔷 redis.asyncio
- [ ] 🔷 Async CRUD
- [ ] 🔷 Async Pub/Sub
- [ ] 🔷 Async Pipelines
- [ ] 🔷 Connection Pooling
- [ ] 🟣 Redis Streams

---

## FastAPI Async

- [ ] 🔷 Async Endpoints
- [ ] 🔷 Async Dependencies
- [ ] 🔷 BackgroundTasks
- [ ] 🔷 Async Database Access
- [ ] 🔷 Async HTTP Calls
- [ ] 🔷 Async File Upload
- [ ] 🔷 WebSockets
- [ ] 🟣 Lifespan Events

---

## Django Async

- [ ] 🔷 Async Views
- [ ] 🔷 ASGI
- [ ] 🔷 Async ORM
- [ ] 🔷 Async Middleware
- [ ] 🔷 Async Signals
- [ ] 🟣 Django Channels

---

## Async Communication

- [ ] 🔷 WebSockets
- [ ] 🔷 Server-Sent Events (SSE)
- [ ] 🔷 Long Polling
- [ ] 🔷 Streaming Responses
- [ ] 🟣 gRPC Async

---

## Performance

- [ ] 🔷 Connection Pooling
- [ ] 🔷 Batch Requests
- [ ] 🔷 Avoid Blocking Code
- [ ] 🔷 Efficient Task Scheduling
- [ ] 🔷 Rate Limiting
- [ ] 🔷 Backpressure
- [ ] 🟣 uvloop

---

## Debugging

- [ ] 🔷 Debug Mode
- [ ] 🔷 Logging Async Code
- [ ] 🔷 Detect Blocking Calls
- [ ] 🔷 Task Inspection
- [ ] 🔷 Stack Traces
- [ ] 🟣 Event Loop Profiling

---

## Common Libraries

- [ ] 🔷 asyncio
- [ ] 🔷 aiohttp
- [ ] 🔷 httpx
- [ ] 🔷 aiofiles
- [ ] 🔷 asyncpg
- [ ] 🔷 redis.asyncio
- [ ] 🔷 SQLAlchemy Async
- [ ] 🟣 uvloop

---

## Async Design Patterns

- [ ] 🔷 Producer Consumer
- [ ] 🔷 Fan-Out
- [ ] 🔷 Fan-In
- [ ] 🔷 Task Queue
- [ ] 🔷 Worker Pool
- [ ] 🔷 Retry Pattern
- [ ] 🔷 Timeout Pattern
- [ ] 🟣 Circuit Breaker

---

## Best Practices

- [ ] 🔷 Use Async for I/O Bound Tasks
- [ ] 🔷 Avoid Blocking Operations
- [ ] 🔷 Await Every Coroutine
- [ ] 🔷 Use Connection Pools
- [ ] 🔷 Handle Timeouts
- [ ] 🔷 Cancel Unused Tasks
- [ ] 🔷 Proper Exception Handling
- [ ] 🔷 Limit Concurrent Tasks
- [ ] 🔷 Use Async Libraries
- [ ] 🟣 Optimize Event Loop

---

## Async Programming Interview Questions

- [ ] 🔷 Async vs Sync
- [ ] 🔷 Concurrency vs Parallelism
- [ ] 🔷 I/O Bound vs CPU Bound
- [ ] 🔷 Coroutine vs Thread
- [ ] 🔷 Event Loop
- [ ] 🔷 async vs await
- [ ] 🔷 asyncio.create_task() vs await
- [ ] 🔷 gather() vs wait()
- [ ] 🔷 Threading vs Asyncio
- [ ] 🔷 Multiprocessing vs Asyncio
- [ ] 🔷 Async SQLAlchemy
- [ ] 🔷 Async FastAPI
- [ ] 🔷 Async File Handling
- [ ] 🔷 Connection Pooling
- [ ] 🔷 Task Cancellation
- [ ] 🔷 Async Context Manager
- [ ] 🔷 Async Generator
- [ ] 🟣 uvloop
- [ ] 🟣 Structured Concurrency
- [ ] 🟣 Event Loop Internals
