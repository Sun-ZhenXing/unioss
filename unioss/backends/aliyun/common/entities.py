from dataclasses import dataclass
from datetime import datetime

from unioss.backends.aliyun.common.enums import StorageClass


@dataclass
class BucketOwner:
    """
    Bucket 的拥有者信息

    References:
        - https://help.aliyun.com/zh/oss/developer-reference/listbuckets
    """

    id: str
    display_name: str


@dataclass
class Bucket:
    """
    Bucket 的信息

    References:
        - https://help.aliyun.com/zh/oss/developer-reference/listbuckets
    """

    name: str
    creation_date: datetime
    location: str
    extranet_endpoint: str
    intranet_endpoint: str
    region: str
    storage_class: StorageClass


@dataclass
class RegionInfo:
    """
    Region 的信息

    References:
        - https://help.aliyun.com/zh/oss/developer-reference/describeregions
    """

    region: str
    internet_endpoint: str
    internal_endpoint: str
    accelerate_endpoint: str
