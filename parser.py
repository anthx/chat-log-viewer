"""
Parses Chat Logs
"""

import csv, sys, locale, codecs
from datetime import datetime, date, time

filename = "Viber_Chats.csv"
def datetime_parser(this_date: str, this_time: str, date_mask="dd/mm/yyyy") -> datetime:
    """
    Parses input dates and outputs a datetime object
    :param this_date:
    :param this_time:
    :param date_mask:
    :return:
    """
    # dt = datetime.strptime(this_date, "%d/%m/%Y")
    dt = datetime.strptime(this_date + this_time, "%d/%m/%Y"+"%H:%M:%S")
    t = datetime.strptime(this_time, "%H:%M:%S")
    # result = datetime.combine(d, t)
    return dt


class Message(object):
    """
    Message class holds and individual message.
    """
    message_id = 0

    def __init__(self, sender_name, sender_number, timestamp, contents):
        """
        Initialises a message with it's contents and metadata
        """
        self._sender_name = sender_name
        self._sender_number = sender_number
        self._timestamp = timestamp
        self.contents = contents
        Message.message_id += 1
        self._id = Message.message_id

    def get_sender_name(self):
        return self._sender_name

    def get_sender_number(self):
        return self._sender_number

    def get_date(self):
        pass

    def get_time(self):
        """
        Getter method for message time
        :return: the time the message was sent
        """
        pass

    @property
    def contents(self):
        return self.__contents

    @contents.setter
    def contents(self, contents):
        self.__contents = contents

    def get_id(self):
        return self._id

    def __repr__(self):
        return f"@{self._timestamp}, {self._sender_name} said, '{self.contents}'"

class ChatLog(object):
    def __init__(self):
        self._messages = {}

    def add_message(self, message):
        self._messages[message.get_id()] = message

    def get_most_recently_found_msg(self) -> Message:
        keys = self._messages.keys()
        highest = sorted(keys)[-1]
        return self._messages[highest]

def main():
    # filename = argv[1]
    viber_chats = ChatLog()
    # print(locale.getpreferredencoding())
    with codecs.open(filename, "r", encoding='utf-8-sig') as chatfile:
        chat = csv.reader(chatfile, delimiter=",")
        for line in chat:
            if len(line) > 1:
                try:
                    timestamp = datetime_parser(line[0], line[1])
                    m = Message(line[2], line[3], timestamp, line[4:])
                    viber_chats.add_message(m)
                except ValueError:
                    viber_chats.get_most_recently_found_msg().contents += line


                print(m)




if __name__  == "__main__":
    # main(sys.argv[1:])
    main()