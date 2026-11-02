# TODO: in-memory stub so alphafund can boot, nothing is persisted. Rebuild on pfeed's IO layer.
from __future__ import annotations

from typing import Any

import datetime
from uuid import UUID, uuid4

import polars as pl
from pfeed.dataflow.result import RunResult


def empty_result() -> RunResult:
    return RunResult(data=pl.DataFrame(), dataflows=[])


def saved_row(id_column: str, id_value: UUID | None = None, **columns: Any) -> RunResult:
    now = datetime.datetime.now(datetime.UTC)
    row = {id_column: str(id_value or uuid4()), "created_at": now, "updated_at": now, "is_deleted": False, **columns}
    return RunResult(data=pl.DataFrame([row]), dataflows=[])
