from st2common.runners.base_action import Action
import pysnow as sn


class BaseAction(Action):
    def __init__(self, config=None, action_service=None):
        super(BaseAction, self).__init__(config, action_service)
        self.client = self._get_client()

    def _get_client(self):
        instance_name = self.config['instance_name']
        username = self.config['username']
        password = self.config['password']

        client = sn.Client(instance=instance_name, user=username, password=password)

        if 'custom_params' in self.config and isinstance(self.config['custom_params'], dict):
            client.parameters.add_custom(self.config['custom_params'])

        return client

    def get_attachments(self, sys_id=None):
        api_path = "/attachment"
        if sys_id:
            api_path += "/{}".format(sys_id)
        r = self.client.resource(api_path=api_path)
        records = r.get(query={})
        return [rec for rec in records.all()]
