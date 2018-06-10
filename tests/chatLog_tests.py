import unittest
from datetime import datetime

from chat_log_parser.parser import ChatLog, Message


class MyTestCase(unittest.TestCase):
    dt1 = datetime.strptime("21/11/2018 16:30", "%d/%m/%Y %H:%M")
    m1 = Message("Alice", "+61 555 555 5555", dt1, "Hello Bob!")
    dt2 = datetime.strptime("21/11/2018 16:32", "%d/%m/%Y %H:%M")
    m2 = Message("Bob", "+61 555 555 7777", dt2, "Hi Alice!")
    dt3 = datetime.strptime("21/11/2018 16:33:14", "%d/%m/%Y %H:%M:%S")
    m3 = Message("Alice", "+61 555 555 5555", dt2, "How are you?")
    dt4 = datetime.strptime("21/11/2018 16:33:25", "%d/%m/%Y %H:%M:%S")
    m4 = Message("Alice", "+61 555 555 5555", dt2, "Are you OK?")


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
        chat = ChatLog()
        chat.add_message(MyTestCase.m1)
        chat.add_message(MyTestCase.m2)
        chat.add_message(MyTestCase.m3)
        self.assertEqual(chat._messages[1].get_sender_name(), "Alice")
        self.assertEqual(chat._messages[2].get_sender_name(), "Bob")
        pass

    def test_date_time_sender(self):
        # the date-time-sender property should work
        actual = MyTestCase.m1.time_date_sender
        expected = "2018-11-21 16:30, Alice"
        self.assertEqual(actual, expected, "time_date_sender property is wrong")
        pass

    def test_date_time_sender_same_minute(self):
        # the date-time-sender property should work
        self.assertEqual(MyTestCase.m3.time_date_sender,
                         MyTestCase.m4.time_date_sender,
                         "date_time_sender isn't removing seconds")
        pass

    def test_day_grouping_one(self):
        pass

    def test_two_days_grouping(self):
        pass

    def test_day_grouping_with_gap(self):
        pass

if __name__ == '__main__':
    unittest.main()
