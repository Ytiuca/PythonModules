"""
This module contains a decorator to time a function execution time
"""

from typing import Callable
from datetime import datetime
from logger import Logger

LOGGER = Logger()


def time_this_function(func: Callable[..., any]) -> Callable:
    """
    This decorator will indicate how long a function took when executed
    """

    def wrapper(*args, **kwargs) -> None:
        # do something before calling the function
        time_before_exec = datetime.now()

        # call the function
        func(*args, **kwargs)

        # do something after calling the function
        time_after_exec = datetime.now()

        duration = time_after_exec - time_before_exec

        LOGGER.info(
            f"the function {func.__name__} took {duration.total_seconds()} to complete"
        )

    return wrapper
