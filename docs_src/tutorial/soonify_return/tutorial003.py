import anyio
import asyncer


async def do_work(name: str):
    await anyio.sleep(1)
    message = f"Hello, {name}"
    return message


async def get_data():
    async with asyncer.create_task_group() as task_group:
        soon_value1 = task_group.soonify(do_work)(name="Yury")
        await anyio.sleep(2)
        if soon_value1.ready:
            print(f"Preview value1: {soon_value1.value}")
        soon_value2 = task_group.soonify(do_work)(name="Nathaniel")
        soon_value3 = task_group.soonify(do_work)(name="Alex")

    data = [soon_value1.value, soon_value2.value, soon_value3.value]
    return data


async def main():
    data = await get_data()
    for message in data:
        print(message)


anyio.run(main)
