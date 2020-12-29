from pynotifier import Notification
import time, pathlib
from courses import Course

class Notifier:
    def __init__(self, title: str, info: str, state):
        self.title, self.info = title, info
        self.status_check = state

    def send(self):
        dir = pathlib.Path(__file__).parent.absolute().as_posix() + '/grouch.ico'
        Notification(
            title=self.title,
            description=self.info,
            icon_path=dir,
            duration=5,
            urgency=Notification.URGENCY_CRITICAL
        ).send()

    def run(self):
        while not self.status_check():
            continue
        self.send()

    def run_async(self):
        if self.status_check():
            self.send()

class WaitlistNotifier(Notifier):
    def __init__(self, course: Course):
        self.title = 'Waitlist Available'
        self.info, self.status_check = course.name, course.waitlist_available
