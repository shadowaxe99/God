```python
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class WebBrowserIntegration:
    def __init__(self):
        self.webSessionData = {}
        self.webBrowser = webdriver.Firefox()

    def navigateWebPage(self, url):
        self.webBrowser.get(url)
        self.webSessionData['webPageLoaded'] = True

    def fillForm(self, form_id, data):
        if self.webSessionData['webPageLoaded']:
            form = self.webBrowser.find_element_by_id(form_id)
            for key, value in data.items():
                form.find_element_by_name(key).send_keys(value)
            form.submit()

    def interactWithWebApp(self, element_id, action):
        if self.webSessionData['webPageLoaded']:
            element = self.webBrowser.find_element_by_id(element_id)
            if action == 'click':
                element.click()
            elif action == 'submit':
                element.submit()

    def performWebSearch(self, search_query):
        self.webBrowser.get('https://www.google.com')
        search_box = self.webBrowser.find_element_by_name('q')
        search_box.send_keys(search_query)
        search_box.submit()

    def closeBrowser(self):
        self.webBrowser.quit()
```