import unittest
import parser


class MyTestCase(unittest.TestCase):
    def test_chat_log_1(self):
        chat = parser.ChatLog()
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
