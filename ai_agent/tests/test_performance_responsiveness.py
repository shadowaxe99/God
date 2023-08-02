```python
import unittest
from ai_agent import main

class TestPerformanceResponsiveness(unittest.TestCase):

    def setUp(self):
        self.ai_agent = main.AI_Agent()

    def test_speed(self):
        import time
        start_time = time.time()
        self.ai_agent.executeCommand('echo "Hello, World!"')
        end_time = time.time()
        execution_time = end_time - start_time
        self.assertTrue(execution_time < 1)

    def test_responsiveness(self):
        import time
        start_time = time.time()
        self.ai_agent.respondToChat('Hello, AI!')
        end_time = time.time()
        response_time = end_time - start_time
        self.assertTrue(response_time < 1)

    def test_resource_usage(self):
        import os
        import psutil
        process = psutil.Process(os.getpid())
        before_memory = process.memory_info().rss / 1024 / 1024
        self.ai_agent.performWebSearch('AI technologies')
        after_memory = process.memory_info().rss / 1024 / 1024
        memory_difference = after_memory - before_memory
        self.assertTrue(memory_difference < 50)

if __name__ == '__main__':
    unittest.main()
```