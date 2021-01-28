from lib.actions import BaseAction


class GetAttachmentsAction(BaseAction):
    def run(self):
        return self.get_attachments()
