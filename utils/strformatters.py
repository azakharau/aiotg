def prepare_method(method: str) -> str:
    return f"/{method}"


def prepare_request_url(url: str, method: str) -> str:
    return f"{url}{prepare_method(method)}"