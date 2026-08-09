"""Small response types that preserve the vendor payload."""

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class MitsubishiResponse:
    """Response metadata and the unmodified JSON payload."""

    status: int
    data: dict[str, Any] | list[Any]
