"""
Service
=======

CRUD methods for services & service groups

"""

from ct_types import Service, ServiceGroup


class Services:

    def __init__(self, CT):

        self.CT = CT

    def list(self):

        res = self.CT.make_request('services')

        services = []
        if res and 'data' in res:
            for item in res['data']:
                services.append(Service(**item))

        return services

    def groups(self):

        res = self.CT.make_request('services')

        sgroups = []
        if res and 'data' in res:
            for item in res['data']:
                sgroups.append(ServiceGroup(**item))

        return sgroups
