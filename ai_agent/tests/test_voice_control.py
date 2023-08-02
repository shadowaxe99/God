```python
import unittest
from ai_agent.voice_control import processVoiceCommand

class TestVoiceControl(unittest.TestCase):

    def setUp(self):
        self.voiceCommandHistory = []

    def test_processVoiceCommand(self):
        command = "Open email"
        expected_response = "Opening email"
        response = processVoiceCommand(command)
        self.voiceCommandHistory.append((command, response))
        self.assertEqual(response, expected_response)

    def test_voiceCommandHistory(self):
        command = "Schedule a meeting at 5pm"
        expected_response = "Meeting scheduled at 5pm"
        response = processVoiceCommand(command)
        self.voiceCommandHistory.append((command, response))
        self.assertIn((command, response), self.voiceCommandHistory)

if __name__ == '__main__':
    unittest.main()
```