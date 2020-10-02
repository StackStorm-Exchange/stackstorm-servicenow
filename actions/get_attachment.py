from lib.actions import BaseAction


class GetAttachmentAction(BaseAction):
    def run(self, table, sys_id):
        s = self.client
        api_path = "/attachment/{}".format(sys_id)
        r = s.resource(api_path=api_path)
        records = r.get(query={})
        output = []
        for record in records.all():
            output.append(record)
        return output
