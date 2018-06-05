import unittest
import parser
from datetime import datetime


class MyTestCase(unittest.TestCase):
    def test_chat_log_1(self):
        chat = parser.ChatLog()
        dt1 = datetime.strptime("21/11/2018 16:30", "%d/%m/%Y %H:%M")
        m1 = parser.Message("Alice", "+61 555 555 5555", dt1, "Hello Bob!")
        chat.add_message(m1)
        expected = "@ ff, Alice said, 'Hello Bob!'"
        self.assertEqual(chat.get_most_recently_found_msg(), expected)


if __name__ == '__main__':
    unittest.main()
