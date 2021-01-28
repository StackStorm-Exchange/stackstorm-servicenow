from lib.actions import BaseAction


class DeleteAction(BaseAction):
    def run(self, table, sysid):
        s = self.client
        r = s.query(table=table, query={'sys_id': sysid})  # pylint: disable=no-member
        response = r.delete()  # pylint: disable=no-member
        return response
