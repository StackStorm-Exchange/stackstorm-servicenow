from lib.actions import BaseAction


class InsertAction(BaseAction):
    def run(self, table, payload):
        response = self.client.insert(table=table, payload=payload)  # pylint: disable=no-member
        return response
