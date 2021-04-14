"""
Service
=======

CRUD methods for services & service groups

"""

from ct_types import Service


class CTService:

    def __init__(self, CT):

        self.CT = CT

    def services(self):

        res = self.CT.make_request('services')

        services = []
        if res and 'data' in res:
            for item in res['data']:
                services.append(Service(item))

        return services
