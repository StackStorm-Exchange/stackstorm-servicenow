from lib.actions import BaseAction


class DeleteAction(BaseAction):
    def run(self, table, sysid):
        r = self.client.query(table=table, query={'sys_id': sys_id}) # pylint: disable=no-member
        response = r.delete()  # pylint: disable=no-member
        return response
