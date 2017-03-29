from lib.actions import BaseAction


class GetNonStructuredAction(BaseAction):
    def run(self, table, query):
        r = self.client.query(table=table, query=str(query))  # pylint: disable=no-member
        response = self.client.get_all()  # pylint: disable=no-member
        output = []
        for each_item in response:
          output.append(each_item)
        return outrp
