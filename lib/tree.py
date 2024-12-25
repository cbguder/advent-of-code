from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, TypeVar

T = TypeVar("T")


@dataclass
class TreeNode[T]:
    value: T
    lhs: Optional[TreeNode[T]]
    rhs: Optional[TreeNode[T]]

    def height(self) -> int:
        lhs_height = 1
        if self.lhs is not None:
            lhs_height = self.lhs.height()

        rhs_height = 1
        if self.rhs is not None:
            rhs_height = self.rhs.height()

        return max(lhs_height, rhs_height) + 1

    def __eq__(self, other: TreeNode[T]) -> bool:
        return (
            (self.value == other.value)
            and (self.lhs == other.lhs)
            and (self.rhs == other.rhs)
        )
