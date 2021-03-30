from functools import partial
import inspect


def curry(function, *curry_args, **curry_kwargs):
    """
    >>> from operator import add
    >>> inc = curry(add, 1)
    >>> inc(12)
    13
    """
    sig = inspect.signature(function)
    try:
        bound = sig.bind(*curry_args, **curry_kwargs)
    except TypeError:
        partial_func = partial(function, *curry_args, **curry_kwargs)
        ret_func = partial(curry, partial_func)
        ret_func.__signature__ = inspect.signature(partial_func)
        return ret_func
    else:
        return function(*bound.args, **bound.kwargs)
