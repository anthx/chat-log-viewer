import unittest
from datetime import datetime

from chat_log_parser.parser import ChatLog, Message


class MyTestCase(unittest.TestCase):
    def test_chat_log_1(self):
        chat = ChatLog()
        dt1 = datetime.strptime("21/11/2018 16:30", "%d/%m/%Y %H:%M")
        m1 = Message("Alice", "+61 555 555 5555", dt1, "Hello Bob!")
        chat.add_message(m1)
        expected = "@2018-11-21 16:30:00, Alice said, 'Hello Bob!'"
        self.assertEqual(str(chat.get_most_recently_found_msg()), expected,
                         "Message doesn't match")


if __name__ == '__main__':
    unittest.main()
