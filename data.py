import times as t


class Log:

    def __init__(self, message):
        self.text = None
        self.timestamp = t.get_timestamp()
        self.message = message

    def get_message(self):
        self.text = self.timestamp + " - " + self.message
        return self.text

# example
# s = "This is the journal"
# L = Log(s)
# print(L.get_message())
