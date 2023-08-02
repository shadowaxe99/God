```python
import unittest
from ai_agent import platform_compatibility

class TestPlatformCompatibility(unittest.TestCase):

    def setUp(self):
        self.platform_compatibility = platform_compatibility.PlatformCompatibility()

    def test_windows_compatibility(self):
        self.assertTrue(self.platform_compatibility.check_compatibility('Windows'))

    def test_mac_compatibility(self):
        self.assertTrue(self.platform_compatibility.check_compatibility('macOS'))

    def test_linux_compatibility(self):
        self.assertTrue(self.platform_compatibility.check_compatibility('Linux'))

    def test_unknown_os_compatibility(self):
        self.assertFalse(self.platform_compatibility.check_compatibility('UnknownOS'))

if __name__ == '__main__':
    unittest.main()
```