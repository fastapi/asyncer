---
name: asyncer
description: Use Asyncer correctly in Python code that mixes async functions, blocking sync functions, worker threads, or concurrent async tasks. Use when choosing between Asyncer, AnyIO, and asyncio patterns; replacing asyncio.gather, AnyIO task groups, to_thread/from_thread calls, or anyio.run wrappers; using asyncer.create_task_group(), TaskGroup.soonify(), SoonValue, asyncify(), syncify(), or runnify(); or avoiding common Asyncer mistakes.
---

# Asyncer Patterns

Use this skill when writing Python code that mixes async functions, blocking sync functions, or concurrent async work and the project depends on `asyncer`.

Asyncer is a small typed layer on top of AnyIO. Prefer the Asyncer helpers below when they fit, because they preserve function signatures, keyword arguments, and return types better than the lower-level AnyIO or asyncio calls.

## Imports

Use one of these styles:

```python
import asyncer
```

```python
from asyncer import asyncify, syncify
```

For task groups, prefer `asyncer.create_task_group()` so the returned task group has Asyncer's extra `soonify()` method.

## Concurrent Async Work

Prefer `asyncer.create_task_group()` plus `task_group.soonify()` for concurrent async function calls.

```python
import asyncer


async def fetch_user(user_id: int) -> User:
    ...


async def load_users(user_ids: list[int]) -> list[User]:
    soon_values: list[asyncer.SoonValue[User]] = []
    async with asyncer.create_task_group() as task_group:
        for user_id in user_ids:
            soon_values.append(task_group.soonify(fetch_user)(user_id=user_id))

    return [soon_value.value for soon_value in soon_values]
```

Use this instead of:

```python
await asyncio.gather(*(fetch_user(user_id) for user_id in user_ids))
```

or raw task creation when the goal is simply "start these async calls concurrently and collect their results".

Do not use `task_group.soon(...)`; Asyncer's API is `task_group.soonify(...)`.
The call shape is:

```python
soon_value = task_group.soonify(async_function)(*args, **kwargs)
```

`soonify()` returns a `SoonValue[T]`. Read `soon_value.value` after the `async with` block, because exiting the task group waits for the scheduled tasks to finish.

```python
async with asyncer.create_task_group() as task_group:
    first = task_group.soonify(fetch_user)(user_id=1)
    second = task_group.soonify(fetch_user)(user_id=2)

users = [first.value, second.value]
```

Inside the same task group, `.value` can raise `PendingValueException` if the task is not complete. If there was an `await` inside the block and you truly need to inspect a value before exiting, check `.ready` first:

```python
async with asyncer.create_task_group() as task_group:
    soon_value = task_group.soonify(fetch_user)(user_id=1)
    await anyio.sleep(0)
    if soon_value.ready:
        user = soon_value.value
```

If code needs to consume values while producer tasks are still running, use a stream/channel pattern instead of `SoonValue.value` inside the task group.

If a task started with `soonify()` raises, the exception propagates when exiting the task group. Do not write code that assumes all `SoonValue.value` results are available after a failed task group unless the failure is caught and handled intentionally.

## Call Sync Code From Async Code

Use `asyncer.asyncify()` when async code must call a blocking sync function without blocking the event loop.

```python
from asyncer import asyncify


def render_pdf(order_id: int) -> bytes:
    ...


async def endpoint(order_id: int) -> Response:
    pdf = await asyncify(render_pdf)(order_id=order_id)
    return Response(pdf, media_type="application/pdf")
```

Use this instead of directly calling blocking functions from async code, and instead of lower-level patterns such as `loop.run_in_executor(...)` or `anyio.to_thread.run_sync(...)` when you want better argument and return typing.

`asyncify()` accepts AnyIO thread options:

```python
result = await asyncify(blocking_call, abandon_on_cancel=True)(item_id=item_id)
```

Use `abandon_on_cancel`, not the deprecated `cancellable` argument. Pass a `limiter=` when the caller needs to limit concurrent worker threads.

## Call Async Code From Sync Code

Use `asyncer.syncify()` from sync code that is running in a worker thread started by async code. A common chain is:

1. An async app or function is running.
2. It calls sync/blocking code with `asyncify()` or a framework-managed worker thread, such as a FastAPI sync endpoint or sync dependency.
3. That sync code needs to call an async function.

```python
from asyncer import asyncify, syncify


async def read_from_async_client(key: str) -> str:
    ...


def sync_business_logic(key: str) -> str:
    value = syncify(read_from_async_client)(key=key)
    return value.upper()


async def handler(key: str) -> str:
    return await asyncify(sync_business_logic)(key=key)
```

Use this instead of `anyio.from_thread.run(...)` when passing keyword arguments or when type support matters.

Do not use `syncify()` inside an async function. In async code, use plain `await` on the async function directly.

For sync functions that must work both from an async worker thread and from a plain sync program, `syncify(..., raise_sync_error=False)` is available:

```python
def sync_business_logic(key: str) -> str:
    return syncify(read_from_async_client, raise_sync_error=False)(key=key)
```

Use this compatibility mode sparingly. Outside a worker thread it starts a new event loop with `anyio.run()`, which is expensive if repeated in a loop. If you need many calls, wrap the loop in one async function and run that once.

## Run An Async Function From Sync Top-Level Code

Use `asyncer.runnify()` when sync top-level code needs to run one async function with positional or keyword arguments and the current thread is not already running an event loop.

```python
import asyncer


async def main(name: str) -> str:
    ...


result = asyncer.runnify(main)(name="World")
```

Use this instead of manually wrapping arguments for `anyio.run(...)`:

```python
result = anyio.run(lambda: main(name="World"))
```

Do not call `runnify()` from a thread that already has a running event loop; from async code, just `await main(...)`.

## Choosing The Asyncer Alternative

Use these replacements by default when Asyncer is available:

- `asyncio.gather(...)` for a batch of async calls with typed results: `asyncer.create_task_group()` plus `task_group.soonify(...)`.
- `anyio.create_task_group().start_soon(...)` for ordinary async function calls: `asyncer.create_task_group().soonify(...)`, especially when kwargs or return values matter.
- `anyio.to_thread.run_sync(...)`, `asyncio.to_thread(...)`, or `loop.run_in_executor(...)`: `await asyncer.asyncify(sync_func)(...)`.
- `anyio.from_thread.run(...)`: `asyncer.syncify(async_func)(...)`.
- `anyio.run(async_func, ...)` from sync top-level code with arguments: `asyncer.runnify(async_func)(...)`.

Still use lower-level AnyIO primitives when Asyncer does not provide the abstraction, such as streams, locks, events, capacity limiters themselves, cancellation scopes, timeouts, or task-group startup handshakes that need `task_status.started()`.

## Common Mistakes

- Do not call blocking sync functions directly from `async def`; wrap them with `await asyncify(sync_func)(...)`.
- Do not use `syncify()` as a general replacement for `await`; it is for sync code, normally in a worker thread started by async code.
- Do not wrap async functions when already in async code; use plain `await async_func(...)`.
- Do not read `SoonValue.value` before the task has completed unless `soon_value.ready` is true.
- Do not instantiate `asyncer.TaskGroup` directly; use `asyncer.create_task_group()`.
