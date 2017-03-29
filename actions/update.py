from lib.actions import BaseAction


class UpdateAction(BaseAction):
    def run(self, table, payload, sysid):
        r = self.client.query(table=table, query={'sys_id': sys_id}).get_one() # pylint: disable=no-member
        response = r.update(payload)  # pylint: disable=no-member
        return response
