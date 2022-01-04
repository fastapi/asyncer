import anyio


async def do_work(name: str):
    await anyio.sleep(1)
    print(f"Hello, {name}")


async def get_data():
    await do_work(name="Yury")
    await do_work(name="Nathaniel")
    await do_work(name="Alex")


async def main():
    await get_data()


anyio.run(main)
