from lib.actions import BaseAction


class InsertAction(BaseAction):
    def run(self, table, payload):
        s = self.client
        response = s.insert(table=table, payload=payload)  # pylint: disable=no-member
        return response
