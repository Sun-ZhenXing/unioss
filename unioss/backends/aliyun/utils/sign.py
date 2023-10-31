import hmac
from base64 import b64encode
from datetime import datetime
from hashlib import md5
from typing import Literal

VERB = Literal["GET", "POST", "PUT", "DELETE", "HEAD", "OPTIONS"]


def _b64_md5(content: str) -> str:
    return b64encode(md5(content.encode()).digest()).decode("utf-8")


def _make_gmt_date(t: datetime) -> str:
    return t.strftime("%a, %d %b %Y %H:%M:%S GMT")


def _get_signature(
    access_key_id: str,
    access_key_secret: str,
    verb: VERB,
    content_md5: str,
    content_type: str,
    date: datetime,
    canonicalized_oss_headers: dict[str, str],
    canonicalized_resource: str,
):
    s = (
        f"{verb}\n"
        f"{content_md5}\n"
        f"{content_type}\n"
        f"{_make_gmt_date(date)}\n"
        f"{canonicalized_oss_headers}{canonicalized_resource}"
    )


def _get_authorization_header_(access_key_id: str, sign: str) -> str:
    return f"OSS {access_key_id}:{sign}"


def _test():
    assert _b64_md5("0123456789") == "eB5eJF1ptWaXm4bijSPyxw=="
    assert (
        _make_gmt_date(datetime(2015, 11, 22, 8, 16, 38))
        == "Sun, 22 Nov 2015 08:16:38 GMT"
    )


if __name__ == "__main__":
    _test()
