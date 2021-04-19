"""
Status
======

CRUD methods for status field

These are the statuses that a person can have.
(e.g. "Visitor", "Friend", "Member", etc.)

"""

from ct_types import CTStatus


class Status:

    def __init__(self, CT):

        self.CT = CT

    def get_all(self):

        res = self.CT.make_request('statuses')

        statuses = []
        if res and 'data' in res:
            for item in res['data']:
                statuses.append(CTStatus(**item))

        return statuses

    def get(self, status_id: int):

        route = f'statuses/{status_id}'
        res = self.CT.make_request(route)

        if res and 'data' in res:
            return CTStatus(**res['data'])

        return None
