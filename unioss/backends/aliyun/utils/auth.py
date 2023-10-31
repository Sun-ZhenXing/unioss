from abc import ABC, abstractmethod


class Auth(ABC):
    """
    授权类
    """

    @abstractmethod
    def get_headers(self) -> dict[str, str]:
        """
        获取请求头
        """
