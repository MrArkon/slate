# Future
from __future__ import annotations

# Standard Library
from typing import TypedDict

# Packages
from typing_extensions import Self


__all__ = (
    "ObsidianChannelMixData",
    "LavalinkChannelMixData",
    "ChannelMix",
)


class ObsidianChannelMixData(TypedDict):
    left_to_left: float
    left_to_right: float
    right_to_left: float
    right_to_right: float


class LavalinkChannelMixData(TypedDict):
    leftToLeft: float
    leftToRight: float
    rightToLeft: float
    rightToRight: float


class ChannelMix:

    def __init__(
        self,
        *,
        left_to_left: float = 1.0,
        left_to_right: float = 0.0,
        right_to_left: float = 0.0,
        right_to_right: float = 1.0,
    ) -> None:

        if any(
                value for value in (left_to_left, left_to_right, right_to_left, right_to_right) if
                value < 0.0 or value > 1.0
        ):
            raise ValueError(
                "'left_to_left', 'left_to_right', 'right_to_left', and 'right_to_right' must all be between "
                "(or equal to) 0.0 and 1.0."
            )

        self.left_to_left: float = left_to_left
        self.right_to_right: float = right_to_right
        self.left_to_right: float = left_to_right
        self.right_to_left: float = right_to_left

    def __repr__(self) -> str:
        return f"<slate.ChannelMix " \
               f"left_to_left={self.left_to_left}, " \
               f"left_to_right={self.left_to_right}, " \
               f"right_to_left={self.right_to_left}, " \
               f"right_to_right{self.right_to_right}>"

    # payload

    def _construct_obsidian_payload(self) -> ObsidianChannelMixData:
        return {
            "left_to_left":   self.left_to_left,
            "left_to_right":  self.left_to_right,
            "right_to_left":  self.right_to_left,
            "right_to_right": self.right_to_right,
        }

    def _construct_lavalink_payload(self) -> LavalinkChannelMixData:
        return {
            "leftToLeft":   self.left_to_left,
            "leftToRight":  self.left_to_right,
            "rightToLeft":  self.right_to_left,
            "rightToRight": self.right_to_right,
        }

    # classmethods

    @classmethod
    def mono(cls) -> Self:
        return cls(left_to_left=0.5, left_to_right=0.5, right_to_left=0.5, right_to_right=0.5)

    @classmethod
    def only_left(cls) -> Self:
        return cls(left_to_left=1.0, left_to_right=0.0, right_to_left=0.0, right_to_right=0.0)

    @classmethod
    def full_left(cls) -> Self:
        return cls(left_to_left=0.5, left_to_right=0.0, right_to_left=0.5, right_to_right=0.0)

    @classmethod
    def only_right(cls) -> Self:
        return cls(left_to_left=0.0, left_to_right=0.0, right_to_left=0.0, right_to_right=1.0)

    @classmethod
    def full_right(cls) -> Self:
        return cls(left_to_left=0.0, left_to_right=0.5, right_to_left=0.0, right_to_right=0.5)

    @classmethod
    def switch(cls) -> Self:
        return cls(left_to_left=0.0, left_to_right=1.0, right_to_left=1.0, right_to_right=0.0)
