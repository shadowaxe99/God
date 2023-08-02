```python
import platform
import sys

def check_platform_compatibility():
    """
    This function checks the compatibility of the AI agent with the user's operating system.
    """
    os_info = platform.uname()
    supported_os = ["Windows", "Linux", "Darwin"]  # Darwin is the name for macOS in Python's platform module

    if os_info.system in supported_os:
        print(f"AI agent is compatible with your {os_info.system} system.")
    else:
        print(f"AI agent is not compatible with your {os_info.system} system.")
        sys.exit()

check_platform_compatibility()
```