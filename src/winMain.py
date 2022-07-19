from multiprocessing.connection import wait
from PyQt5.QtWidgets import *
from PyQt5 import uic
from courses import *
import threading
# import multiprocessing
from datetime import datetime

courses = {}
# openCourse = []
# waitlistCourse = []
fullList = []

class Ui(QDialog):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('src\qtWin.ui', self) # Load the .ui file
        
        self.courseList = self.findChild(QScrollArea, 'courseList')
        self.courseList.setWidget(QListWidget())

        self.addBtn = self.findChild(QPushButton, 'addCourse')
        self.addBtn.clicked.connect(self.newCourse)

        self.track = self.findChild(QPushButton, 'startTracking')
        self.track.clicked.connect(self.startTrack)

        self.show() # Show the GUI
    
    def newCourse(self):
        crn = self.findChild(QLineEdit, 'CRN').text()
        sem = self.findChild(QComboBox, 'term').currentText()
        
        now = datetime.now()
        term = ""
        if sem.lower() == 'spring':
            term = f'{now.year + 1}' + '02' if now.month > 4 else f'{now.year}' + '02'
        else:
            term = f'{now.year}' + '05' if sem.lower() == 'summer' else f'{now.year}' + '08'

        # typeTrack = self.findChild(QComboBox, 'trackType').currentText()
        # print(crn, sem, term, typeTrack)
        crs = Course(crn, term)
        fullList.append(crs)
        # courses[crs] = typeTrack
        self.courseList.widget().addItem(f"{crs.name} | {sem}")

    def startTrack(self):
        # for c in courses.keys():
        #     if courses[c] == "Open Seats":
        #         openCourse.append(c)
        #     else:
        #         # has to be Open Waitlist, only two options on dropdown
        #         waitlistCourse.append(c)
    
        # all notifiers created
        # we can now watch the sun set on a grateful universe
        self.close()
            

    
app = QApplication([])
win = Ui()
win.setWindowTitle("Grouch UI")
app.exec_()
app.exit()

# openCList = CourseList(openCourse)
# openWList = CourseList(waitlistCourse)

# multiprocessing.Process(target=openCList.run_available_courses).start()
# multiprocessing.Process(target=openWList.run_waitlist_notifiers).start()
# threading.Thread(target=openCList.run_available_courses).start()
# threading.Thread(target=openWList.run_waitlist_notifiers).start()

# print("woooooo")

# fullList = openCourse + waitlistCourse
CourseList(fullList).run_notifiers()

# while True:
#     pass