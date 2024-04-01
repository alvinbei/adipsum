def call_until(max_attempts, func, *args, **kwargs):
    """Calls a function until it succeeds or the max number of attempts is reached.

    Args:
        max_attempts: The maximum number of attempts to make.
        func: The function to call.
        *args: The positional arguments to pass to the function.
        **kwargs: The keyword arguments to pass to the function.

    Returns:
        The result of the function call.

    Raises:
        AssertionError: If max_attempts is less than 1.
        Exception: If the function call fails and the maximum number of attempts is reached.
    """

    assert max_attempts >= 1, "max_attempts must be greater than or equal to 1"

    for attempt in range(1, max_attempts + 1):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if attempt == max_attempts:
                raise e

