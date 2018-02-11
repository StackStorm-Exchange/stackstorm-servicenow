from st2common.runners.base_action import Action
import pysnow as sn


class BaseAction(Action):
    def __init__(self, config):
        super(BaseAction, self).__init__(config)
        self.client = self._get_client()

    def _get_client(self):
        instance_name = self.config['instance_name']
        username = self.config['username']
        password = self.config['password']

        s = sn.Client(instance=instance_name, user=username, password=password)

        if 'custom_params' in self.config:
            s.parameters.add_custom(self.config['custom_params'])

        return s
