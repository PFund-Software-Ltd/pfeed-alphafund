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
from pfeed_alphafund.chat.data_model import AlphaFundChatDataModel


# TODO: stub, nothing is persisted
class AlphaFundChatFeed(BaseFeed["AlphaFund", "BaseRequest", AlphaFundChatDataModel]):
    class Requests:  # ty: ignore[invalid-attribute-override]
        download: ClassVar[None] = None
        retrieve: ClassVar[None] = None
        stream: ClassVar[None] = None

    DataModel: ClassVar[type[AlphaFundChatDataModel]] = AlphaFundChatDataModel  # ty: ignore[invalid-mutable-override]
    data_domain: ClassVar[DataCategory] = DataCategory.CHAT_DATA

    @classmethod
    def create_data_model(cls, *args: Any, **kwargs: Any) -> AlphaFundChatDataModel:
        raise NotImplementedError(f"{cls.__name__}.create_data_model() is not implemented yet")

    def _get_default_transformations(self, request: BaseRequest, /) -> list[Callable[..., Any]]:
        raise NotImplementedError(f"{type(self).__name__} has no verbs yet")

    def run(self, use_prefect: bool = False, **prefect_kwargs: Any) -> Any:
        raise NotImplementedError(f"{type(self).__name__} has no verbs yet")

    def retrieve(self, **filters: Any) -> RunResult:
        return empty_result()

    def save_channel(self, **columns: Any) -> RunResult:
        return saved_row("channel_id")

    def save_chat(self, chat_id: Any = None, is_deleted: bool = False, **columns: Any) -> RunResult:
        return saved_row("chat_id", chat_id, is_deleted=is_deleted)

    def save_message(self, message_id: Any = None, **columns: Any) -> RunResult:
        return saved_row("message_id", message_id)

    def retrieve_embeddings(self, embedding_model: str, columns: list[str] | None = None) -> RunResult:
        return empty_result()

    def save_embeddings(self, **columns: Any) -> RunResult:
        return empty_result()

    def create_search_index(self, embedding_model: str) -> None:
        pass

    def search(self, embedding_model: str, **kwargs: Any) -> RunResult:
        return empty_result()
