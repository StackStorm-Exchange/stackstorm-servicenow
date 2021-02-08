from lib.actions import BaseAction


class GetAction(BaseAction):
    def run(self, table, query, fields=[]):
        # If using new ServiceNew API...
        if self.config['use_new_service_now_api'] == True:
            client = self.client
            resource = client.resource(api_path="/table/{0}".format(table))
            if not fields:
                response = resource.get(query=query)
            else:
                response = resource.get(query=query, fields=fields)
            output = []
            for each_item in response.all():
                output.append(each_item)
            return output

        s = self.client
        r = s.query(table=table, query=query)  # pylint: disable=no-member
        response = r.get_all()  # pylint: disable=no-member
        output = []
        for each_item in response:
            output.append(each_item)
        return output
