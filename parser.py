"""
Parses Chat Logs
"""

import csv, sys, locale, codecs
from datetime import datetime, date, time
from jinja2 import Environment, BaseLoader, FileSystemLoader, select_autoescape, exceptions
from dateutil.parser import *
# from dateutil.tz import *
from datetime import *

# filename = "Viber_Chats.csv"

env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

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

    def __init__(self, sender_name, sender_number, timestamp, contents) -> None:
        """
        Initialises a message with it's contents and metadata
        """
        self._sender_name = sender_name
        self._sender_number = sender_number
        self.timestamp = timestamp
        # self._contents = ""
        self.contents: str = contents
        Message.message_id += 1
        self._id = Message.message_id

    @property
    def is_user(self):
        return self._is_user

    @is_user.setter
    def is_user(self, flag):
        self._is_user = flag

    def get_sender_name(self):
        return self._sender_name

    def get_sender_number(self):
        return self._sender_number

    @property
    def time_date_sender(self):
        time_part: str = str(self.timestamp.time())[:5]
        return f"{self.timestamp.date()} {time_part}, {self._sender_name}"

    @property
    def contents(self):
        return self._contents

    @contents.setter
    def contents(self, contents):
        # for each in contents_list:
        #     self._contents = self._contents + ", " + each
        self._contents = contents

    def get_id(self):
        return self._id

    def __repr__(self):
        return f"@{self.timestamp}, {self._sender_name} said, '{self.contents}'"

class ChatLog(object):
    def __init__(self):
        self._messages = {}

    def add_message(self, message):
        self._messages[message.get_id()] = message

    def get_most_recently_found_msg(self) -> Message:
        keys = self._messages.keys()
        highest = sorted(keys)[-1]
        return self._messages[highest]


def viber(filename, viber_chats):
    with codecs.open(filename, "r", encoding='utf-8-sig') as chatfile:
        chat = csv.reader(chatfile, delimiter=",")
        for line in chat:
            if len(line) > 0:
                try:
                    timestamp = datetime_parser(line[0], line[1])
                    content = ""
                    for i, message_fragment in enumerate(line[4:]):
                        content += message_fragment
                        if i + 1 != len(line[4:]):
                            content += ", "
                    m = Message(line[2], line[3], timestamp, content)
                    if m.get_sender_name() == 'Me':
                        m.is_user = True
                    viber_chats.add_message(m)
                except (ValueError, IndexError):
                    # this must be a continuation of the previous message
                    rest_content = "\n"
                    if len(line) == 0: print("here")
                    for i, message_fragment in enumerate(line):
                        rest_content += message_fragment
                        if i + 1 != len(line):
                            rest_content += ", "
                    viber_chats.get_most_recently_found_msg().contents += rest_content
            elif len(line) == 0:
                # this must be a continuation of the previous message
                # and a para space
                viber_chats.get_most_recently_found_msg().contents += "\n"


def kakao(filename, kakao_chats):
    with codecs.open(filename, "r", encoding='utf-8-sig') as chatfile:
        chat = csv.reader(chatfile, delimiter=",")
        # the KakaoTalk chatlog export includes headers.
        # Maybe I'll parse them later. For now, just skip over the first 2 lines
        next(chatfile)
        next(chatfile)
        next(chatfile)
        next(chatfile)
        for line in chat:
            if len(line) > 2:
                try:
                    timestamp = timestamp = parse(line[0] + line[1])
                    content = ""
                    # KakaoTalk separates the sender and message
                    # in the 2nd csv value so we need to separate them specially
                    sender, sep, message = "".join(line[2:]).partition(" : ")

                    # for i, message_fragment in enumerate(line[4:]):
                    #     content += message_fragment
                    #     if i + 1 != len(line[4:]):
                    #         content += ", "
                    m = Message(sender.strip(), 0, timestamp, message.strip())
                    if m.get_sender_name() == 'you':
                        m.is_user = True
                    kakao_chats.add_message(m)
                except (ValueError, IndexError):
                    # this must be a continuation of the previous message
                    rest_content = "\n"
                    if len(line) == 0: print("here")
                    for i, message_fragment in enumerate(line):
                        rest_content += message_fragment
                        if i + 1 != len(line):
                            rest_content += ", "
                    kakao_chats.get_most_recently_found_msg().contents += rest_content
            elif len(line) == 0:
                # this must be a continuation of the previous message
                # and a para space
                kakao_chats.get_most_recently_found_msg().contents += "\n"


def messenger(filename, messenger_chat):
    with codecs.open(filename, "r") as chatfile:
        chat = csv.reader(chatfile, delimiter=",")
        # the Facebook chatlog parser includes headers.
        # Maybe I'll parse them later. For now, just skip over the first line
        next(chatfile)
        for line in chat:
            if len(line) > 1:
                try:
                    timestamp = parse(line[2])
                    m = Message(line[1], 0, timestamp, line[3])
                    messenger_chat.add_message(m)
                except ValueError:
                    # this must be a continuation of the previous message
                    rest_content = "\n"
                    for i, message_fragment in enumerate(line):
                        rest_content += message_fragment
                        if i + 1 != len(line):
                            rest_content += ", "
                    messenger_chat.get_most_recently_found_msg().contents = rest_content


def main(argv):
    filename = argv[0]
    application = argv[1]
    chat = ChatLog()
    # print(locale.getpreferredencoding())
    # print(filename)
    if application == "viber":
        viber(filename, chat)
    if application == "messenger":
        messenger(filename, chat)
    if application == "kakao":
        kakao(filename, chat)

    try:
        template = env.get_template(f"{application}.html")
        output = (template.render(chat=chat))

        with open(f"chat_log_{application}.html", 'wb') as f:
            f.write(output.encode("utf-8"))
    except exceptions.TemplateNotFound:
        print("Template not found")





if __name__  == "__main__":
    main(sys.argv[1:])
    # main()