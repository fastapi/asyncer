import anyio


async def do_work(name: str):
    await anyio.sleep(1)
    return f"Hello, {name}"


async def main():
    message = await do_work(name="World")
    return message


result = anyio.run(main)
print(result)
