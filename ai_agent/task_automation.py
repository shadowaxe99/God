```python
import schedule
from datetime import datetime
from ai_agent.local_computer_control import executeCommand

taskQueue = []

class Task:
    def __init__(self, command, time):
        self.command = command
        self.time = time

def scheduleTask(task):
    schedule.every().day.at(task.time).do(executeCommand, task.command)
    taskQueue.append(task)

def runTasks():
    while True:
        schedule.run_pending()

def addTask(command, time):
    task = Task(command, time)
    scheduleTask(task)

def removeTask(task):
    if task in taskQueue:
        taskQueue.remove(task)
        return True
    return False

def getTaskQueue():
    return taskQueue
```