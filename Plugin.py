from abc import ABC, abstractmethod

class Plugin(ABC):
    @abstractmethod
    def display_content(self, content):
        pass

#=========================================================
      
class TextPlugin(Plugin):
    def display_content(self, content):
        print(f"Displaying text content: {content.lower()}")

#=========================================================

class ImagePlugin(Plugin):
    def display_content(self, content):
        print(f"Displaying Image content: {content.upper()}")     

#=========================================================

class Browser:
    def __init__(self):
        self.plugins = []

    def add_plugin(self, plugin):
        self.plugins.append(plugin)

    def display_content(self, content):
        for plugin in self.plugins:
            plugin.display_content(content)

#=========================================================
# Implementation
            
browser = Browser()
browser.add_plugin(TextPlugin())
browser.add_plugin(ImagePlugin())

#=========================================================

browser.display_content("Hello, world!")

