import sys
from courses import Course, CourseList
from datetime import datetime

if len(sys.argv) < 3:
    print("Could not run Grouch; include the desired upcoming term (Fall, Spring, Summer) and use at least one CRN")
    sys.exit(1)

season = sys.argv[1]
now = datetime.now()
term = ''

if season.lower() == 'spring':
    term = f'{now.year + 1}' + '02' if now.month > 4 else f'{now.year}' + '02'
else:
    term = f'{now.year}' + '05' if season.lower() == 'summer' else f'{now.year}' + '08'

crns = sys.argv[2:]
courses = [Course(crn, term) for crn in crns]

lst = CourseList(courses)
lst.run_notifiers()
