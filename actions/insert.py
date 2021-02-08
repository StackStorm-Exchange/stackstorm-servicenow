from lib.actions import BaseAction


class InsertAction(BaseAction):
    def run(self, table, payload):
        # If using new ServiceNew API...
        if self.config['use_new_service_now_api'] == True:
            client = self.client
            resource = client.resource(api_path="/table/{0}".format(table))
            response = resource.create(payload=payload)  # pylint: disable=no-member
            return response

        s = self.client
        response = s.insert(table=table, payload=payload)  # pylint: disable=no-member
        return response
