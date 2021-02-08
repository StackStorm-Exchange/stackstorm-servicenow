from lib.actions import BaseAction


class DeleteAction(BaseAction):
    def run(self, table, sysid):
        # If using new ServiceNew API...
        if self.config['use_new_service_now_api'] == True:
            client = self.client
            resource = client.resource(api_path="/table/{0}".format(table))
            response = resource.delete(query={"sys_id": sysid})  # pylint: disable=no-member
            return response

        s = self.client
        r = s.query(table=table, query={'sys_id': sysid})  # pylint: disable=no-member
        response = r.delete()  # pylint: disable=no-member
        return response
