```python
import os
from cryptography.fernet import Fernet
from ai_agent.user_interface import userPreferences

class SecuritySchema:
    def __init__(self, user):
        self.user = user
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

    def encrypt_data(self, data):
        encrypted_data = self.cipher_suite.encrypt(data)
        return encrypted_data

    def decrypt_data(self, encrypted_data):
        decrypted_data = self.cipher_suite.decrypt(encrypted_data)
        return decrypted_data

securitySettings = SecuritySchema(userPreferences)

def protectData(data):
    encrypted_data = securitySettings.encrypt_data(data)
    return encrypted_data

def accessProtectedData(encrypted_data):
    decrypted_data = securitySettings.decrypt_data(encrypted_data)
    return decrypted_data

def checkUserPermissions(resource):
    user_permissions = userPreferences.get('permissions', {})
    resource_permissions = user_permissions.get(resource, None)
    if resource_permissions:
        return True
    else:
        return False

def securityAlert(message):
    print(f"Security Alert: {message}")
```