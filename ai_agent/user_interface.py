```python
import tkinter as tk
from tkinter import messagebox
from .local_computer_control import executeCommand
from .task_automation import scheduleTask
from .chat_interaction import respondToChat
from .web_browser_integration import navigateWebPage, performWebSearch
from .voice_control import processVoiceCommand
from .personalization_learning import learnFromInteraction
from .security_privacy import protectData

class UserInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Multi-Functional AI Agent")
        self.create_widgets()

    def create_widgets(self):
        self.command_entry = tk.Entry(self.root)
        self.command_entry.pack()

        self.submit_button = tk.Button(self.root, text="Submit", command=self.process_input)
        self.submit_button.pack()

    def process_input(self):
        user_input = self.command_entry.get()
        if user_input.startswith("cmd:"):
            executeCommand(user_input[4:])
        elif user_input.startswith("task:"):
            scheduleTask(user_input[5:])
        elif user_input.startswith("chat:"):
            respondToChat(user_input[5:])
        elif user_input.startswith("web:"):
            if "search:" in user_input:
                performWebSearch(user_input[5:])
            else:
                navigateWebPage(user_input[5:])
        elif user_input.startswith("voice:"):
            processVoiceCommand(user_input[6:])
        elif user_input.startswith("learn:"):
            learnFromInteraction(user_input[6:])
        elif user_input.startswith("protect:"):
            protectData(user_input[8:])
        else:
            messagebox.showerror("Error", "Invalid command")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    ui = UserInterface()
    ui.run()
```