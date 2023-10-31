from dataclasses import dataclass

from unioss.backends.aliyun.common.entities import Bucket, BucketOwner


@dataclass
class ListAllMyBucketsResult:
    """
    `ListBuckets` 操作的返回结果.

    Refer: https://help.aliyun.com/zh/oss/developer-reference/listbuckets
    """

    Bucketowner: BucketOwner
    buckets: list[Bucket]
    prefix: str | None = None
    marker: str | None = None
    max_keys: int | None = None
    is_truncated: bool | None = None
