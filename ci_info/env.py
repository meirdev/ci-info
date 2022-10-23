import abc
import os


class Env(abc.ABC):
    @abc.abstractmethod
    def __bool__(self) -> bool:  # pragma: no cover
        ...


class EnvExists(Env):
    def __init__(self, key: str) -> None:
        self.key = key

    def __bool__(self) -> bool:
        return self.key in os.environ


class EnvNotExists(EnvExists):
    def __bool__(self) -> bool:
        return not super().__bool__()


class EnvEqual(Env):
    def __init__(self, key: str, value: str) -> None:
        self.key = key
        self.value = value

    def __bool__(self) -> bool:
        return os.environ.get(self.key) == self.value


class EnvNotEqual(EnvEqual):
    def __bool__(self) -> bool:
        return not super().__bool__()


class EnvList:
    def __init__(self, *env: Env) -> None:
        self.env = env


class EnvAny(EnvList):
    def __bool__(self) -> bool:
        return any(self.env)


class EnvAll(EnvList):
    def __bool__(self) -> bool:
        return all(self.env)
