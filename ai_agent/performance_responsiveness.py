```python
import time
import psutil
from threading import Thread

class PerformanceMonitor:
    def __init__(self):
        self.start_time = time.time()
        self.cpu_usage = 0
        self.memory_usage = 0
        self.disk_usage = 0
        self.monitor_thread = Thread(target=self.monitor_performance)
        self.monitor_thread.start()

    def monitor_performance(self):
        while True:
            self.cpu_usage = psutil.cpu_percent(interval=1)
            self.memory_usage = psutil.virtual_memory().percent
            self.disk_usage = psutil.disk_usage('/').percent
            time.sleep(1)

    def get_performance_data(self):
        return {
            'uptime': time.time() - self.start_time,
            'cpu_usage': self.cpu_usage,
            'memory_usage': self.memory_usage,
            'disk_usage': self.disk_usage
        }

performance_monitor = PerformanceMonitor()
```