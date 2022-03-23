from lib.actions import BaseAction


class UploadAttachmentAction(BaseAction):
    def run(self, table, file, sysid):
        s = self.client
        r = s.query(table=table, query={'sys_id': sysid})  # pylint: disable=no-member
        response = r.attach(file)  # pylint: disable=no-member
        return response
