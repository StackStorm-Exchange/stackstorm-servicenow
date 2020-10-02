from lib.actions import BaseAction


class GetAttachmentsAction(BaseAction):
    def run(self, table):
        s = self.client
        r = s.resource(api_path="/attachment")
        records = r.get(query={})
        output = []
        for record in records.all():
            output.append(record)
        return output
