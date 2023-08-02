```python
import requests
from .security_privacy import protectData

class InternetAccess:
    def __init__(self):
        self.webSessionData = {}

    def retrieveInformation(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                self.webSessionData[url] = response.text
                return response.text
            else:
                return None
        except Exception as e:
            print(f"Error retrieving information: {e}")
            return None

    def performWebSearch(self, query):
        try:
            search_url = f"https://www.google.com/search?q={query}"
            response = requests.get(search_url)
            if response.status_code == 200:
                self.webSessionData[search_url] = response.text
                return response.text
            else:
                return None
        except Exception as e:
            print(f"Error performing web search: {e}")
            return None

    def accessExternalDataSource(self, url, userPermissions):
        if userPermissions.get('externalDataAccess', False):
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    protectedData = protectData(response.text)
                    self.webSessionData[url] = protectedData
                    return protectedData
                else:
                    return None
            except Exception as e:
                print(f"Error accessing external data source: {e}")
                return None
        else:
            print("User does not have permission to access external data sources.")
            return None
```