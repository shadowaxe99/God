```python
import unittest
from ai_agent import personalization_learning

class TestPersonalizationLearning(unittest.TestCase):

    def setUp(self):
        self.learningData = personalization_learning.LearningData()

    def test_learn_from_interaction(self):
        interaction_data = {
            "interactionType": "voiceCommand",
            "command": "open browser",
            "response": "Opening browser"
        }
        self.learningData.learn_from_interaction(interaction_data)
        self.assertIn(interaction_data, self.learningData.learningData)

    def test_update_user_preferences(self):
        new_preferences = {
            "preferredBrowser": "Firefox",
            "preferredVoice": "Female"
        }
        self.learningData.update_user_preferences(new_preferences)
        self.assertEqual(self.learningData.userPreferences, new_preferences)

    def test_get_user_preferences(self):
        preferences = self.learningData.get_user_preferences()
        self.assertEqual(preferences, self.learningData.userPreferences)

    def test_get_learning_data(self):
        learning_data = self.learningData.get_learning_data()
        self.assertEqual(learning_data, self.learningData.learningData)

if __name__ == '__main__':
    unittest.main()
```