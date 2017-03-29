from lib.actions import BaseAction


class AssignIncidentToAction(BaseAction):
    def run(self, user_id, number):
        s = self.client
        r = s.query(table='incident', query={'number': number}).get_one()
        response = r.update({'assigned_to': user_id})
        return response
