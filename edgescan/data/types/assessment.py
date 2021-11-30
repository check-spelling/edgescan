from dataclasses import dataclass
from typing import Optional, List, Union
from edgescan.data.types.object import Object

import hodgepodge.time
import datetime


@dataclass(frozen=True)
class Assessment(Object):
    id: int
    type: str
    status: str
    created_at: datetime.datetime

    @property
    def create_time(self) -> datetime.datetime:
        return self.created_at

    def matches(
            self,
            ids: Optional[List[int]] = None,
            types: Optional[List[str]] = None,
            statuses: Optional[List[str]] = None,
            min_create_time: Optional[Union[str, int, float, datetime.datetime, datetime.date]] = None,
            max_create_time: Optional[Union[str, int, float, datetime.datetime, datetime.date]] = None) -> bool:

        #: Filter by assessment ID.
        if ids and self.id not in ids:
            return False

        #: Filter by assessment type.
        if types and self.type not in types:
            return False

        #: Filter by assessment status.
        if statuses and self.status not in statuses:
            return False

        #: Filter assessments based on when they were last performed.
        if (min_create_time or max_create_time) and \
                not hodgepodge.time.in_range(self.create_time, minimum=min_create_time, maximum=max_create_time):
            return False
        return True

    def __hash__(self):
        return self.id
