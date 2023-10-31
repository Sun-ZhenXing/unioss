from enum import Enum, auto


class StorageClass(Enum):
    """
    Bucket 存储类型，支持 `Standard`、`IA`、`Archive` 和 `ColdArchive` 四种存储类型.

    分别对应的是标准存储、低频访问存储、归档存储和冷归档存储.
    """

    Standard = auto()
    IA = auto()
    Archive = auto()
    ColdArchive = auto()


class ObjectErrorCode(Enum):
    """
    Object 对象的错误码
    """

    MissingContentLength = auto()  # 411
    InvalidEncryptionAlgorithmError = auto()  # 400
    AccessDenied = auto()  # 403
    NoSuchBucket = auto()  # 404
    InvalidObjectName = auto()  # 400
    InvalidArgument = auto()  # 400
    RequestTimeout = auto()  # 400
    BadRequest = auto()  # 400
    KmsServiceNotEnabled = auto()  # 403
    FileAlreadyExists = auto()  # 409
    FileImmutable = auto()  # 409
