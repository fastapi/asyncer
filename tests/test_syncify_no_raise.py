import threading
from dataclasses import dataclass
from typing import List

import anyio
from asyncer import asyncify, syncify


@dataclass
class Report:
    thread_id: int
    caller_func: str


def test_syncify_no_raise_async():
    reports: List[Report] = []

    async def do_sub_async_work():
        report = Report(
            thread_id=threading.get_ident(),
            caller_func="do_sub_async_work",
        )
        reports.append(report)

    def do_sub_sync_work():
        report = Report(
            thread_id=threading.get_ident(),
            caller_func="do_sub_sync_work",
        )
        reports.append(report)
        syncify(do_sub_async_work, raise_sync_error=False)()

    async def do_async_work():
        report = Report(
            thread_id=threading.get_ident(),
            caller_func="do_async_work",
        )
        reports.append(report)
        await asyncify(do_sub_sync_work)()

    def do_sync_work():
        own_report = Report(
            thread_id=threading.get_ident(),
            caller_func="do_sync_work",
        )
        reports.append(own_report)
        syncify(do_async_work, raise_sync_error=False)()

    async def main():
        own_report = Report(
            thread_id=threading.get_ident(),
            caller_func="main",
        )
        reports.append(own_report)
        await asyncify(do_sync_work)()

    def sync_main():
        own_report = Report(
            thread_id=threading.get_ident(),
            caller_func="sync_main",
        )
        reports.append(own_report)
        do_sync_work()

    anyio.run(main)
    sync_main()
    main_thread_id = threading.get_ident()
    assert reports[0].caller_func == "main"
    assert reports[0].thread_id == main_thread_id
    assert reports[1].caller_func == "do_sync_work"
    assert reports[1].thread_id != main_thread_id
    assert reports[2].caller_func == "do_async_work"
    assert reports[2].thread_id == main_thread_id
    assert reports[3].caller_func == "do_sub_sync_work"
    assert reports[3].thread_id != main_thread_id
    assert reports[4].caller_func == "do_sub_async_work"
    assert reports[4].thread_id == main_thread_id
    assert reports[5].caller_func == "sync_main"
    assert reports[5].thread_id == main_thread_id
    assert reports[6].caller_func == "do_sync_work"
    assert reports[6].thread_id == main_thread_id
    assert reports[7].caller_func == "do_async_work"
    assert reports[7].thread_id == main_thread_id
    assert reports[8].caller_func == "do_sub_sync_work"
    assert reports[8].thread_id != main_thread_id
    assert reports[9].caller_func == "do_sub_async_work"
    assert reports[9].thread_id == main_thread_id
