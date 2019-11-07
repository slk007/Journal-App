import timing as t


class log:

    def __init__(self, message):
        self.text = None
        self.timestamp = t.get_stamp()
        self.message = message

    def set_message(self):
        self.text = self.timestamp + " - " + self.message

    def get_message(self):
        return self.text

