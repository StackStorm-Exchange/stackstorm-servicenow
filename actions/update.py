from lib.actions import BaseAction


class UpdateAction(BaseAction):
    def run(self, table, payload, sysid):
        s = self.client
        r = s.query(table=table, query={'sys_id': sysid}).get_one()  # pylint: disable=no-member
        response = r.update(payload)  # pylint: disable=no-member
        return response
