from __future__ import annotations

from typing import TYPE_CHECKING, Any, ClassVar

if TYPE_CHECKING:
    from pfeed.base.feed import BaseFeed

from uuid import UUID

from pfeed.enums import DataAccessType, DataCategory, DataProviderType
from pfeed.source import BaseSource, SourceMetadata

from pfeed_alphafund.agent.feed import AlphaFundAgentFeed
from pfeed_alphafund.chat.feed import AlphaFundChatFeed
from pfeed_alphafund.fund.feed import AlphaFundFundFeed


class AlphaFund(BaseSource):
    Feeds: ClassVar[dict[DataCategory, type[BaseFeed]]] = {
        DataCategory.FUND_DATA: AlphaFundFundFeed,
        DataCategory.AGENT_DATA: AlphaFundAgentFeed,
        DataCategory.CHAT_DATA: AlphaFundChatFeed,
    }
    metadata: ClassVar[SourceMetadata] = SourceMetadata(
        name="ALPHAFUND",
        url="https://pfund.ai",
        data_categories={
            DataCategory.FUND_DATA: {},
            DataCategory.AGENT_DATA: {},
            DataCategory.CHAT_DATA: {},
        },
        provider_type=DataProviderType.VENUE,
        access_type=DataAccessType.FREE,
    )

    fund_feed: AlphaFundFundFeed
    agent_feed: AlphaFundAgentFeed
    chat_feed: AlphaFundChatFeed

    def __init__(self, fund_id: UUID | str | None = None, **kwargs: Any):
        self._fund_id = UUID(str(fund_id)) if fund_id is not None else None
        super().__init__(**kwargs)

    @property
    def fund_id(self) -> UUID | None:
        return self._fund_id
