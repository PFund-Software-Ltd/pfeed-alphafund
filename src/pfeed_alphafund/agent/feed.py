from __future__ import annotations

from typing import TYPE_CHECKING, Any, ClassVar

if TYPE_CHECKING:
    from collections.abc import Callable

    from pfeed.base.request import BaseRequest
    from pfeed.dataflow.result import RunResult

    from pfeed_alphafund.source import AlphaFund  # noqa: F401, used as a string forward reference in the class bases

from pfeed.base.feed import BaseFeed
from pfeed.enums import DataCategory

from pfeed_alphafund._stub import empty_result, saved_row
from pfeed_alphafund.agent.data_model import AlphaFundAgentDataModel


# TODO: stub, nothing is persisted
class AlphaFundAgentFeed(BaseFeed["AlphaFund", "BaseRequest", AlphaFundAgentDataModel]):
    class Requests:  # ty: ignore[invalid-attribute-override]
        download: ClassVar[None] = None
        retrieve: ClassVar[None] = None
        stream: ClassVar[None] = None

    DataModel: ClassVar[type[AlphaFundAgentDataModel]] = AlphaFundAgentDataModel  # ty: ignore[invalid-mutable-override]
    data_domain: ClassVar[DataCategory] = DataCategory.AGENT_DATA

    @classmethod
    def create_data_model(cls, *args: Any, **kwargs: Any) -> AlphaFundAgentDataModel:
        raise NotImplementedError(f"{cls.__name__}.create_data_model() is not implemented yet")

    def _get_default_transformations(self, request: BaseRequest, /) -> list[Callable[..., Any]]:
        raise NotImplementedError(f"{type(self).__name__} has no verbs yet")

    def run(self, use_prefect: bool = False, **prefect_kwargs: Any) -> Any:
        raise NotImplementedError(f"{type(self).__name__} has no verbs yet")

    def retrieve(self, **filters: Any) -> RunResult:
        return empty_result()

    def save_agent(self, fund_id: Any, agent_name: str, agent_role: Any, agent_class: str) -> RunResult:
        return saved_row("agent_id", agent_name=agent_name)
