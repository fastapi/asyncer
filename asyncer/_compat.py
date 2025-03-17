import inspect
from typing import Callable, TypeVar, Union

import anyio
import anyio.to_thread
from anyio import CapacityLimiter
from typing_extensions import TypeVarTuple, Unpack

T_Retval = TypeVar("T_Retval")
PosArgsT = TypeVarTuple("PosArgsT")

# Use abandon_on_cancel if available
RUN_SYNC_AOC = (
    "abandon_on_cancel" in inspect.getfullargspec(anyio.to_thread.run_sync).kwonlyargs
)


async def run_sync(
    func: Callable[[Unpack[PosArgsT]], T_Retval],
    *args: Unpack[PosArgsT],
    abandon_on_cancel: bool = False,
    limiter: Union[CapacityLimiter, None] = None,
) -> T_Retval:
    # AnyIO 4.1.0 renamed cancellable to abandon_on_cancel
    if RUN_SYNC_AOC:
        return await anyio.to_thread.run_sync(
            func, *args, abandon_on_cancel=abandon_on_cancel, limiter=limiter
        )
    else:
        return await anyio.to_thread.run_sync(
            func, *args, cancellable=abandon_on_cancel, limiter=limiter
        )
