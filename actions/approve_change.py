from lib.actions import BaseAction


class ApprovalAction(BaseAction):
    def run(self, number):
        s = self.client
        r = s.query(table='change_request', query={'number': number}).get_one()
        response = r.update({'approval': 'approved'})
        return response
