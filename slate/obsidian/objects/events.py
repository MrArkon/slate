# Future
from __future__ import annotations

# Standard Library
from typing import Any

# My stuff
from ...objects.enums import ErrorSeverity, EventType, TrackEndReason


__all__ = [
    "ObsidianBaseEvent",
    "ObsidianTrackStart",
    "ObsidianTrackEnd",
    "ObsidianTrackStuck",
    "ObsidianTrackException",
    "ObsidianWebsocketOpen",
    "ObsidianWebsocketClosed"
]


class ObsidianBaseEvent:

    def __init__(
        self,
        data: dict[str, Any]
    ) -> None:

        self._type: EventType = EventType(data["type"])
        self._guild_id: int = int(data["guild_id"])

    def __repr__(self) -> str:
        return f"<slate.ObsidianBaseEvent guild_id='{self.guild_id}'>"

    #

    @property
    def type(self) -> EventType:
        return self._type

    @property
    def guild_id(self) -> int:
        return self._guild_id

    #


class ObsidianTrackStart(ObsidianBaseEvent):

    def __init__(
        self,
        data: dict[str, Any]
    ) -> None:

        super().__init__(data)

        self._track_id: str = data["track"]

    def __repr__(self) -> str:
        return f"<slate.ObsidianTrackStart guild_id='{self.guild_id}' track_id='{self.track_id}'>"

    #

    @property
    def track_id(self) -> str:
        return self._track_id


class ObsidianTrackEnd(ObsidianBaseEvent):

    def __init__(
        self,
        data: dict[str, Any]
    ) -> None:

        super().__init__(data)

        self._track_id: str = data["track"]

        self._reason: TrackEndReason = TrackEndReason(data["reason"])

    def __repr__(self) -> str:
        return f"<slate.ObsidianTrackEnd guild_id='{self.guild_id}' track_id='{self.track_id}' reason={self.reason}>"

    #

    @property
    def track_id(self) -> str:
        return self._track_id

    @property
    def reason(self) -> TrackEndReason:
        return self._reason


class ObsidianTrackStuck(ObsidianBaseEvent):

    def __init__(
        self,
        data: dict[str, Any]
    ) -> None:

        super().__init__(data)

        self._track_id: str = data["track"]

        self._threshold_ms: int = data["threshold_ms"]

    def __repr__(self) -> str:
        return f"<slate.ObsidianTrackStuck guild_id='{self.guild_id}' track_id='{self.track_id}' threshold_ms={self.threshold_ms}>"

    #

    @property
    def track_id(self) -> str:
        return self._track_id

    @property
    def threshold_ms(self) -> int:
        return self._threshold_ms


class ObsidianTrackException(ObsidianBaseEvent):

    def __init__(
        self,
        data: dict[str, Any]
    ) -> None:

        super().__init__(data)

        self._track_id: str = data["track"]

        exception: dict[str, Any] = data["exception"]
        self._message: str = exception["message"]
        self._cause: str = exception["cause"]
        self._severity: ErrorSeverity = ErrorSeverity(data["severity"])

    def __repr__(self) -> str:
        return f"<slate.ObsidianTrackException guild_id='{self.guild_id}' track_id='{self.track_id}' " \
               f"severity='{self.severity}' cause='{self.cause}' message='{self.message}'>"

    #

    @property
    def track_id(self) -> str:
        return self._track_id

    @property
    def message(self) -> str:
        return self._message

    @property
    def cause(self) -> str:
        return self._cause

    @property
    def severity(self) -> ErrorSeverity:
        return self._severity


class ObsidianWebsocketOpen(ObsidianBaseEvent):

    def __init__(
        self,
        data: dict[str, Any]
    ) -> None:

        super().__init__(data)

        self._target: str = data["target"]
        self._ssrc: int = data["ssrc"]

    def __repr__(self) -> str:
        return f"<slate.ObsidianWebsocketOpen>"

    #

    @property
    def target(self) -> str:
        return self._target

    @property
    def ssrc(self) -> int:
        return self._ssrc


class ObsidianWebsocketClosed(ObsidianBaseEvent):

    def __init__(
        self,
        data: dict[str, Any]
    ) -> None:

        super().__init__(data)

        self._code: int = data["code"]
        self._reason: str = data["reason"]
        self._by_remote: bool = data["by_remote"]

    def __repr__(self) -> str:
        return f"<slate.ObsidianWebsocketClosed>"

    #

    @property
    def code(self) -> int:
        return self._code

    @property
    def reason(self) -> str:
        return self._reason

    @property
    def by_remote(self) -> bool:
        return self._by_remote
