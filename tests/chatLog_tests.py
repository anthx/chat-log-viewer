import unittest
from datetime import datetime

from chat_log_parser.parser import ChatLog, Message


class MyTestCase(unittest.TestCase):
    dt1 = datetime.strptime("21/11/2018 16:30", "%d/%m/%Y %H:%M")
    m1 = Message("Alice", "+61 555 555 5555", dt1, "Hello Bob!")
    dt2 = datetime.strptime("21/11/2018 16:32", "%d/%m/%Y %H:%M")
    m2 = Message("Bob", "+61 555 555 7777", dt2, "Hi Alice!")
    dt3 = datetime.strptime("21/11/2018 16:33", "%d/%m/%Y %H:%M")
    m3 = Message("Alice", "+61 555 555 5555", dt2, "How are you?")

    def test_chat_log_1(self):
        chat = ChatLog()
        chat.add_message(MyTestCase.m1)
        expected = "@2018-11-21 16:30:00, Alice said, 'Hello Bob!'"
        self.assertEqual(str(chat.get_most_recently_found_msg()), expected,
                         "Message doesn't match")

    def test_chat_log_2(self):
        chat = ChatLog()
        chat.add_message(MyTestCase.m1)
        chat.add_message(MyTestCase.m2)
        expected = "@2018-11-21 16:32:00, Bob said, 'Hi Alice!'"
        self.assertEqual(str(chat.get_most_recently_found_msg()), expected,
                         "Message doesn't match")

    def test_order(self):
        # test they come out in right order
        pass

    def test_date_time_sender(self):
        # the date-time-sender property should work
        pass

    def test_date_time_sender_same_minute(self):
        # the date-time-sender property should work
        pass

    def test_day_grouping_one(self):
        pass

    def test_two_days_grouping(self):
        pass

    def test_day_grouping_with_gap(self):
        pass

if __name__ == '__main__':
    unittest.main()
