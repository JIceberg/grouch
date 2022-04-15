# Grouch

## About

A registration aid for [Oscar](https://oscar.gatech.edu). Simple, effective, and customizable. No login necessary. Grouch is a Python library for getting registration info for all your classes. It sends notifications using [py-notifier](https://pypi.org/project/py-notifier/) to your computer.

Oscar is a garbage site, but at least they allow students to see course info without logging in (thanks to a little trick I picked up from [Sana](https://github.com/CrimsonMarten)'s snipe bot). It's important to note that web scraping is extremely unstable since websites are updated often &mdash; even Oscar, which might be shocking considering it looks and feels like it's from the early 2000s. Literally any minor change to the layout or names or style can screw the entire scraping process. If something goes wrong, please open an issue ASAP so I can get it fixed.

## Installation

To use this project, you need Python 3.8+ installed as well as pip on your device.

* Clone the library `git clone https://github.com/JIceberg/grouch.git`

* Open the root of the project and open a CLI (command line interface) like powershell

* Install the necessary requirements `pip install -r requirements-<os>.txt` (note that mac users need to use requirements-unix.txt)

And that's it! The library is now installed and ready to be used.

## Usage

### Tracker

The simplest usage is to simply run `python src/tracker.py [SEASON] CRN-1 CRN-2 ...` in the CLI.
For the season, use 'spring', 'fall', or 'summer'. An example call is below
```sh
user@computer:~$ python src/tracker.py fall 82693 89515 ...
```

If you're a bit more advanced (i.e. you know at least some basic Python 3), then you can
use the tools in the library to configure your own notifications and reminders. Grouch
comes equipped with `notifier` and `courses` handlers for easy use.

An example of a custom program would be
```python
from courses import Course, WaitlistNotifier

myCourse = Course(crn, 'fall')
notif = WaitlistNotifier(myCourse)

notif.run()
```
To run it, just do `python path/to/file.py`.

### Info

From the CLI, run `python src/info.py [SEASON] CRN-1 CRN-2 ...` and a notification will be sent
containing information for the class. This does not loop, unlike the tracker.
