from lib.actions import BaseAction


class UpdateAction(BaseAction):
    def run(self, table, payload, sysid):
        # If using new ServiceNew API...
        if self.config['use_new_service_now_api']:
            client = self.client
            resource = client.resource(api_path="/table/{0}".format(table))
            response = resource.update(query={"sys_id": sysid}, payload=payload)  # pylint: disable=no-member
            return response

        s = self.client
        r = s.query(table=table, query={'sys_id': sysid})  # pylint: disable=no-member
        response = r.update(payload)  # pylint: disable=no-member
        return response
