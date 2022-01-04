import anyio
import asyncer


async def do_work(name: str):
    await anyio.sleep(1)
    print(f"Hello, {name}")


async def get_data():
    async with asyncer.create_task_group() as task_group:
        task_group.soonify(do_work)(name="Yury")
        task_group.soonify(do_work)(name="Nathaniel")
        task_group.soonify(do_work)(name="Alex")


async def main():
    await get_data()


anyio.run(main)
