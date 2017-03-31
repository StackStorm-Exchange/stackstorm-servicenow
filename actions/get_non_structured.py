from lib.actions import BaseAction


class GetNonStructuredAction(BaseAction):
    def run(self, table, query):
        s = self.client
        r = s.query(table=table, query=str(query))  # pylint: disable=no-member
        response = r.get_all()  # pylint: disable=no-member
        output = []
        for each_item in response:
            output.append(each_item)
        return output
