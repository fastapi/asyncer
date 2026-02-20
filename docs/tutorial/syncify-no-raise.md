# Syncify - In Mainly Sync Code

We used `syncify()` in the previous chapter assuming that the main program was **async**.

That means that whatever code was calling `syncify()` was at some previous point called with `asyncify()`.

In other words, the main program was started in some way with something like:

```Python
anyio.run(main)
```

And then down the line something called `asyncify()`, and then inside of that, something called `syncify()`.

But there could be cases where you need to be able to have a **sync** function that calls **async** code correctly, and that still **works regardless** of if the main program is **async** or **sync**.

## Run Async Code from Mainly Blocking Code

By default, when using **Asyncer**'s `syncify()`, it will expect to be called from a *worker thread*. That normally means from some code that was initially called with `asyncify()`.

If you use `syncify()` directly in a mainly **sync** (blocking) program, by default, AnyIO will raise an exception telling you that it expects to be called from a *worker thread*.

But `syncify()` has an **option** that you can set: `raise_sync_error=False`, that instead of raising an error will **run the async code**:

{* docs_src/tutorial/syncify_no_raise/tutorial001_py310.py hl[14] *}

If `syncify()` is called from inside of an async program (so, from inside of some code called with `asyncify()`), it will do the same thing as always, send the async function from the **worker thread** to the **main async thread** and run it there.

But if the program is not async, when using `syncify(raise_sync_error=False)`, it will run the async function as if it was starting from scratch, with `anyio.run()`.

## Start an Async and Sync Program

In this example, in the same file, we are running both an async and a sync program.

{* docs_src/tutorial/syncify_no_raise/tutorial001_py310.py hl[28:30] *}

* We first run the async code, with `anyio.run()`. It starts the async function `main()`.
* Then we run the sync code, we just call directly `sync_main()`.

In this example, because `do_sync_work()` will be called from **async code** and from **sync code**, we need it to always *work* and in any way, run the async function with `syncify()`, returning the value. Even if it means that underneath it will have to start a full new async execution with `anyio.run()`.

## Computational Cost

Running many times something like `anyio.run()` frequently from a mainly sync program could be expensive, as every time it has to start a new *event loop*, etc.

If your program is mainly sync and you use `syncify(raise_sync_error=False)` that will run `anyio.run()`.

There are some cases where you just **need** that to happen for compatibility of the code mixing async and sync code.

But have in mind that if you call that multiple times (for example in a `for` loop) it will probably be expensive.

If you need to call `syncify(raise_sync_error=False)` many times, for example in a `for` loop, consider wrapping that `for` loop in a single async function, and calling that one instead.
