from lib.actions import BaseAction


class CreateRecordAction(BaseAction):
    def run(self, table, payload):
        s = self.client

        path = '/table/{0}'.format(table)
        response = s.resource(api_path=path).create(payload=payload)  # pylint: disable=no-member
        return 

