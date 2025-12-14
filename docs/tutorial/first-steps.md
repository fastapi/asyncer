# First Steps with AnyIO

Asyncer is based on **AnyIO**, so let's start with a simple example just using **AnyIO** to write async code.

## A Main Function

Let's start with a simple main async function.

{* docs_src/tutorial/first_steps/tutorial001.py ln[9:11] hl[9:10] *}

When working with **async** code you normally use `async` and `await`.

The main rules are that:

* You can only use `await` inside `async` functions.
* To call an `async` function, you need to use `await` in front of it.

In this case, we can use `await` inside of `main()` because it is an `async` function.

## Call Async Functions

The function `do_work()` also needs to be declared with `async def` for us to be able to `await` for its result when calling it.

`do_work()` could be talking to a **database**, calling an **API**, or something else that needs to wait for something.

For this example, let's simulate that by making `do_work()` wait there for 1 second:

{* docs_src/tutorial/first_steps/tutorial001.py ln[4:11] hl[4:5] *}

## Run the Main Function

As `main()` is an `async` function, we can't call it directly because we can't `await` it. Instead, we call it with `anyio.run()`:

{* docs_src/tutorial/first_steps/tutorial001.py hl[1,14] *}

`anyio.run()` will do everything necessary to call `main()`, handling all the `await` parts, and waiting there until it finishes.

## Run the Program in the Command Line

If you run that, you will see the expected result, it will **wait for 1 second** and then print `Hello, World`:

<div class="termy">

```console
$ python main.py

// Wait for it...

// After around one second
Hello, World
```

</div>

## Next Steps

Great! That's already a **first async program**. 🚀

Now let's start updating the example and see in which cases **Asyncer** could be **useful**.
