from __future__ import annotations

from datetime import datetime, timedelta, timezone

BRASILIA_OFFSET = timezone(timedelta(hours=-3))


def utc_now_naive() -> datetime:
    """Return UTC now as naive datetime for broad DB compatibility."""
    return datetime.now(timezone.utc).replace(tzinfo=None)


def format_datetime_brt(value: datetime | None, fmt: str = '%d/%m/%Y %H:%M') -> str:
    if not value:
        return '-'
    if value.tzinfo is None:
        value = value.replace(tzinfo=timezone.utc)
    return value.astimezone(BRASILIA_OFFSET).strftime(fmt)
