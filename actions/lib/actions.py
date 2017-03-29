from st2actions.runners.pythonrunner import Action
import pysnow as sn


class BaseAction(Action):
    def __init__(self, config):
        super(BaseAction, self).__init__(config)
        self.client = self._get_client()

    def _get_client(self, default_payload=None):
        instance_name = self.config['instance_name']
        username = self.config['username']
        password = self.config['password']
        if self.config['default_payload']:
            default_payload = self.config['default_payload']

        return sn.Client(instance_name, username, password, default_payload=default_payload)

    def get_client_with_default_payload(default_payload):
        self.client = self._get_client(default_payload)
