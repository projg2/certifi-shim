"""
A thin replacement for certifi Python module that uses system
certificate store.
"""


def where():
    return "/etc/ssl/certs/ca-certificates.crt"


def contents():
    with open(where(), "r") as f:
        return f.read()
