import anyio
import asyncer


async def do_work(name: str):
    await anyio.sleep(1)
    return f"Hello, {name}"


async def main(name: str):
    result = await do_work(name=name)
    return result


result = asyncer.runnify(main)(name="World")
print(result)
