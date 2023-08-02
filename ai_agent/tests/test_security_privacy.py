```python
import unittest
from ai_agent import security_privacy

class TestSecurityPrivacy(unittest.TestCase):

    def setUp(self):
        self.security_privacy = security_privacy.SecurityPrivacy()
        self.userPreferences = {"privacy": "high", "security": "high"}
        self.securitySettings = {"dataEncryption": True, "firewall": True}

    def test_protectData(self):
        self.security_privacy.protectData(self.userPreferences, self.securitySettings)
        self.assertTrue(self.security_privacy.dataProtected)

    def test_checkUserPermissions(self):
        self.security_privacy.checkUserPermissions(self.userPreferences)
        self.assertTrue(self.security_privacy.permissionsChecked)

    def test_enforcePrivacySettings(self):
        self.security_privacy.enforcePrivacySettings(self.userPreferences)
        self.assertTrue(self.security_privacy.privacyEnforced)

    def test_enforceSecuritySettings(self):
        self.security_privacy.enforceSecuritySettings(self.securitySettings)
        self.assertTrue(self.security_privacy.securityEnforced)

if __name__ == '__main__':
    unittest.main()
```