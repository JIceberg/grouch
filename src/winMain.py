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
fullDict = {}

# TODO: MAKE THING SO THEY CAN REMOVE CRNs 

class Ui(QDialog):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('src\qtWin.ui', self) # Load the .ui file
        
        # find QScrollArea (list where courses added to)
        self.courseList = self.findChild(QScrollArea, 'courseList')
        self.courseList.setWidget(QListWidget())

        # binding button to method
        self.addBtn = self.findChild(QPushButton, 'addCourse')
        self.addBtn.clicked.connect(self.newCourse)

        # binding term button to method
        self.termBtn = self.findChild(QPushButton, 'setTerm')
        self.termBtn.clicked.connect(self.tSet)

        # binding button to close window method, starts tracking courses
        self.track = self.findChild(QPushButton, 'startTracking')
        self.track.clicked.connect(self.close)

        self.dCourse = self.findChild(QPushButton, "delCourse")
        self.dCourse.clicked.connect(self.rmvCourse)

        self.term = ""

        self.show() # Show the GUI
    
    def newCourse(self):
        if self.term == "":
            # check if user confirmed/set a term to search for CRNs during
            alrt = QMessageBox()
            alrt.setWindowTitle("Error")
            alrt.setText(f"Term not set (choose from dropdown and click \"Set Term\")")
            x = alrt.exec_()

        else: 
            crn = self.findChild(QLineEdit, 'CRN').text()
            
            try:
                # create Course item and add to list to be tracked
                crs = Course(crn, self.term)
                # add to dictionary for fast removal if necessary
                fullDict[crn] = crs
                
                # add item to list in QScrollArea
                self.courseList.widget().addItem(crs.name)
            except IndexError:
                # means something wacky happened and oscar didn't have course
                alrt = QMessageBox()
                alrt.setWindowTitle("Error")
                alrt.setText(f"CRN {crn} not found")
                x = alrt.exec_()

    def tSet(self):
        # grab the term from dropdown
        sem = self.findChild(QComboBox, 'term').currentText()
        now = datetime.now()

        # use parsing definitely not ctrl-c ctrl-v from tracking.py to change fall/spring/summer to a oscar acceptable format
        if sem.lower() == 'spring':
            self.term = f'{now.year + 1}' + '02' if now.month > 4 else f'{now.year}' + '02'
        else:
            self.term = f'{now.year}' + '05' if sem.lower() == 'summer' else f'{now.year}' + '08'

        # changing label to reflect term
        self.findChild(QLabel, 'curTerm').setText(f"Current Term: {sem}")

        # small popup to confirm term set
        # gets annoying after a while though
        # alrt = QMessageBox()
        # alrt.setWindowTitle("Term Set!")
        # alrt.setText(f"Term set to {self.term} ({sem})")
        # x = alrt.exec_()

    def rmvCourse(self):
        # track all selected indices in QScrollArea
        selected = self.courseList.widget().selectedIndexes()
        # for each selection, grab data, remove CRN from fullDict (won't track) and remove from QScrollArea
        for ind in selected:
            inf = ind.data()
            crn = inf.split(" - ")[1]
            fullDict.pop(crn)
            self.courseList.widget().takeItem(ind.row())
            

# generic driver code
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

# create CourseList of courses and run notifiers
# future goal: use multithreading or something to concurrently run waitlist and open course trackers (wasn't able to initially get working)
# so you can track waitlists of some sections (i.e. lab blocks) while checking openings of others (i.e. general lecture blocks)
fullList = [fullDict[x] for x in fullDict.keys()]
CourseList(fullList).run_notifiers()
