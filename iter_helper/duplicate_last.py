from typing import Generic, List, TypeVar

T = TypeVar("T")


class DuplicateLast(Generic[T]):
    def __init__(self, *arg: T):
        self.args = arg

    def __len__(self)->int:
        return len(self.args)

    def __getitem__(self, n: int)->T:
        return self.args[n] if len(self) > n else self.args[-1]
