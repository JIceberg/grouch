import subprocess
import time, pathlib

CMD = '''
on run argv
  display notification (item 2 of argv) with title (item 1 of argv)
end run
'''

class Notifier:
    def __init__(self, title: str, info: str, state):
        self.title, self.info = title, info
        self.status_check = state

    def __init__(self, title: str, info: str):
        self.title, self.info = title, info

    def send(self):
        title = self.title
        text = self.info
        subprocess.call(['osascript', '-e', CMD, title, text])
        time.sleep(7)

    def run(self):
        while not self.status_check():
            continue
        self.send()

    def run_async(self):
        if self.status_check():
            self.send()

    def run_force(self):
        self.send()
