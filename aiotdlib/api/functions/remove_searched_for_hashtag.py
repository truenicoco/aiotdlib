# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class RemoveSearchedForHashtag(BaseObject):
    """
    Removes a hashtag or a cashtag from the list of recently searched for hashtags or cashtags

    :param hashtag: Hashtag or cashtag to delete
    :type hashtag: :class:`String`
    """

    ID: typing.Literal["removeSearchedForHashtag"] = Field(
        "removeSearchedForHashtag", validation_alias="@type", alias="@type"
    )
    hashtag: String
