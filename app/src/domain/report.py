from hashlib import sha256
from typing import Optional
from json import dumps


class Report:
    """Report is a special entity which contains information about some kind of
    problem."""

    headers: dict
    body: Optional[dict]
    hash: int

    def __init__(
        self, headers: dict, body: dict = {}, hash_value: Optional[int] = None
    ):
        self.body = body
        self.headers = headers
        if hash_value is not None:
            self.hash = hash_value
        else:
            self.hash = _create_hash(headers, body)

    def to_dict(self) -> dict:
        return {"body": self.body, "headers": self.headers, "hash": self.hash}

    def __repr__(self):
        return str(self.to_dict())

    def __eq__(self, o):
        return self.to_dict() == o.to_dict()


def _create_hash(headers: dict, body: dict = {}) -> int:
    """Generate non-random hash."""
    content = {"headers": headers, "body": body}
    string = dumps(content, sort_keys=True)
    return int(sha256(string.encode("utf-8")).hexdigest()[:8], 16)
