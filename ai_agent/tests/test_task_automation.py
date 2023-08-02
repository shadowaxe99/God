```python
import unittest
from ai_agent import task_automation

class TestTaskAutomation(unittest.TestCase):

    def setUp(self):
        self.taskQueue = task_automation.TaskQueue()
        self.task = task_automation.Task('Test Task', 'executeCommand', ['ls'])

    def test_scheduleTask(self):
        self.taskQueue.scheduleTask(self.task)
        self.assertIn(self.task, self.taskQueue.tasks)

    def test_executeTask(self):
        self.taskQueue.scheduleTask(self.task)
        self.taskQueue.executeTask(self.task)
        self.assertNotIn(self.task, self.taskQueue.tasks)

    def test_taskCompleted(self):
        self.taskQueue.scheduleTask(self.task)
        self.taskQueue.executeTask(self.task)
        self.assertIn('taskCompleted', self.taskQueue.messages)

if __name__ == '__main__':
    unittest.main()
```