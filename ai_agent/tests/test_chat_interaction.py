```python
import unittest
from ai_agent import chat_interaction

class TestChatInteraction(unittest.TestCase):

    def setUp(self):
        self.chatHistory = chat_interaction.chatHistory
        self.respondToChat = chat_interaction.respondToChat

    def test_chat_history(self):
        self.assertIsInstance(self.chatHistory, list)

    def test_respond_to_chat(self):
        response = self.respondToChat("Hello AI")
        self.assertIsInstance(response, str)
        self.assertIn(response, self.chatHistory)

    def test_chat_schema(self):
        for chat in self.chatHistory:
            self.assertIsInstance(chat, chat_interaction.ChatSchema)

if __name__ == '__main__':
    unittest.main()
```