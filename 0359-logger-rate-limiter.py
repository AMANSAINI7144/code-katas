class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.messages = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message not in self.messages:
            self.messages[message] = timestamp
            return True
        else:
            if timestamp - self.messages[message] >= 10:
                self.messages[message] = timestamp
                return True
            else:
                return False
