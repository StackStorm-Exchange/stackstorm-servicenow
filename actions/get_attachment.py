from lib.actions import BaseAction


class GetAttachmentAction(BaseAction):
    def run(self, sys_id):
        return self.get_attachments(sys_id)
