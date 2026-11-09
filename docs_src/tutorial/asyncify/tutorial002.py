import time

import anyio
from asyncer import asyncify


def do_sync_work(name: str):
    time.sleep(1)
    return f"Hello, {name}"


async def main():
    message = await asyncify(do_sync_work)(name="World")
    print(message)


anyio.run(main)
