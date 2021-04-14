"""
Status
======

CRUD methods for status field

"""

from ct_types import Status


class CTStatus:

    def __init__(self, CT):

        self.CT = CT

    def get_all(self):

        res = self.CT.make_request('statuses')

        statuses = []
        if res and 'data' in res:
            for item in res['data']:
                statuses.append(Status(item))

        return statuses

    def get(self, status_id: int):

        route = f'statuses/{status_id}'
        res = self.CT.make_request(route)

        if res and 'data' in res:
            return Status(res['data'])

        return None
