def compose(*functions):
    """
    >>> from operator import neg, abs
    >>>
    >>> assert compose(neg) is neg
    >>> assert compose(neg, abs)(-5) == -5
    """
    head, *tail = functions
    return head if not tail else lambda *args, **kwargs: head(compose(*tail)(*args, **kwargs))


def starred(function):
    def wrapper(iterator):
        return function(*iterator)
    return wrapper
