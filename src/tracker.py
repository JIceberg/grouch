import sys
from courses import Course, CourseList

if len(sys.argv) < 2:
    sys.exit(1)

crns = sys.argv[1:]
courses = [Course(crn) for crn in crns]

lst = CourseList(courses)
lst.run_notifiers()
