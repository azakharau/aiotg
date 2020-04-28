def prepare_method(method: str) -> str:
    """

    Args:
        method:

    Returns:

    """
    return f"/{method}"


def create_request_url(url: str, method: str) -> str:
    """

    Args:
        url:
        method:

    Returns:

    """
    return f"{url}{prepare_method(method)}"


def create_request_url_with_params(url: str,
                                   method: str,
                                   **kwargs) -> str:
    """

    Args:
        url:
        method:
        **kwargs:

    Returns:

    """
    if not kwargs:
        raise ValueError("Request parameters not specified")

    request_url = f"{create_request_url(url, method)}?"

    for param_name, value in kwargs.items():
        if param_name == next(reversed(list(kwargs))):  # if last element
                                                        # in kwargs - don't
                                                        # add "&" in query
            request_url += f"{param_name}={value}"
            return request_url

        request_url += f"{param_name}={value}&"
