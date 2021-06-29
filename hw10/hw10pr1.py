# CS5 Gold/Black: Homework 10 Problem 1
# Filename: hw10pr1.py
# Name: Paul Burke
# Problem description: Classy Programming!


class Date:
    """A user-defined data structure that
       stores and manipulates dates.
    """

    def __init__(self, month, day, year):
        """Construct a Date with the given month, day, and year."""
        self.month = month
        self.day = day
        self.year = year

    def __repr__(self):
        """This method returns a string representation for the
           object of type Date that calls it (named self).

           ** Note that this function _can_ be called explicitly, but
              it more often is used implicitly via the print statement
              or simply by expressing self's value.
        """
        d = self.day
        m = self.month
        y = self.year
        string = f"{m:02d}/{d:02d}/{y:04d}"
        return string

    def isLeapYear(self):
        """Returns True if the calling object is
           in a leap year; False otherwise."""
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False

    def copy(self):
        """Returns a new object with the same month, day, year
           as the calling object (self).
        """
        dnew = Date(self.month, self.day, self.year)
        return dnew

    def equals(self, d2):
        """Decides whether self and d2 represent the same calendar date,
           regardless of whether they are in the same place in memory.
        """
        if self.year == d2.year and self.month == d2.month \
                    and self.day == d2.day:    # The backslash allows this on a new line!
            return True
        else:
            return False

    def __eq__(self, d2):
        """Overrides the == operator so that it declares two of the same dates
           in history as ==.  This way , we don't need to use the awkward
           d.equals(d2) syntax...
        """
        if self.year == d2.year and self.month == d2.month \
               and self.day == d2.day:
            return True
        else:
            return False

    def isBefore(self, d2):
        """
            returns True if self is before d2, False otherwise
        """
        if self.year < d2.year:
            return True
        elif self.month < d2.month and self.year == d2.year:
            return True
        elif self.day < d2.day and self.year == d2.year and self.month == d2.month:
            return True
        else:
            return False

    def __lt__(self, d2):
        """If self is before d2, this should
        return True; else False """

        return self.isBefore(d2)

    def isAfter(self, d2):
        """
            returns True if self is after d2, False otherwise
        """
        return d2.isBefore(self)

    def __gt__(self, d2):
        """greater than (self is after than d2)"""
        return d2.isBefore(self)

    def tomorrow(self):
        """ moves the self date ahead 1 day"""
        fdays = 28 + self.isLeapYear()
        DIM = [0, 31, fdays, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.day += 1
        if self.day > DIM[self.month]:
            self.day = 1
            self.month += 1
            if self.month == 13:
                self.month = 1
                self.year += 1

    def yesterday(self):
        """ moves the self date back 1 day"""
        fdays = 28 + self.isLeapYear()
        DIM = [31, fdays, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # got rid of the 0
        self.day -= 1
        if self.day < 1:
            self.day =  DIM[self.month-2] # still works because wraps around
            self.month -= 1
            if self.month < 1:
                self.month = 12
                self.year -= 1

    def addNDays(self, N):
        """ adds N days to self date"""
        for i in range(N):
            self.tomorrow()
            print(f"{self.month:02d}/{self.day:02d}/{self.year:04d}")

    def __iadd__(self, N):
        addNDays(self, N)
        return self

    def subNDays(self, N):
        """ subtracts N days to self date"""
        for i in range(N):
            self.yesterday()
            print(f"{self.month:02d}/{self.day:02d}/{self.year:04d}")

    def __isub__(self, N):
        subNDays(self, N)
        return self

    def diff(self, d2):
        """ difference in days between self and d2"""
        self_1 = self.copy()
        c = 0
        if self.isBefore(d2):
            while not self_1 == d2:
                c -= 1
                self_1.tomorrow()
        elif self.isAfter(d2):
            while not self_1 == d2:
                c += 1
                self_1.yesterday()
        return c

    def dow(self):
        """ get date of the week that self is on"""
        dow = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        DIM = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        total_days = 365*self.year + sum(DIM[:self.month-1]) + self.day
        leap_days = self.year // 4 - self.year // 100 + self.year // 400
        total_days += leap_days
        return dow[total_days % 7 - 2]


# nycounter() computes in the next 100 years, what day of the week January 1st falls on
# it returns a list of the days of the week and how many January 1sts there are for each
# 14 for each except friday and saturday which are 15 times
def nycounter():
    """Looking ahead to 100 years of NY celebrations..."""

    dowd = {}              # dowd == 'day of week dictionary'
    dowd["Sunday"] = 0     # a 0 entry for Sunday
    dowd["Monday"] = 0     # and so on...
    dowd["Tuesday"] = 0
    dowd["Wednesday"] = 0
    dowd["Thursday"] = 0
    dowd["Friday"] = 0
    dowd["Saturday"] = 0

    # Live for another 100 years...
    for year in range(2021, 2121):
        d = Date(1, 1, year)   # Get new year
        print('Current date is', d)
        s = d.dow()        # Get day of week
        dowd[s] += 1       # Count it

    print('Totals are', dowd)


# bdaycounter() computes in the next 100 years, what day of the week my birthday (April 16th) falls on
# it returns a list of the days of the week and how many April 16ths there are for each
# 14 for each except friday and saturday which are 15 times
def bdaycounter():
    """Looking ahead to 100 years of birthdays celebrations..."""

    dowd = {}              # dowd == 'day of week dictionary'
    dowd["Sunday"] = 0     # a 0 entry for Sunday
    dowd["Monday"] = 0     # and so on...
    dowd["Tuesday"] = 0
    dowd["Wednesday"] = 0
    dowd["Thursday"] = 0
    dowd["Friday"] = 0
    dowd["Saturday"] = 0

    # Live for another 100 years...
    for year in range(2021, 2121):
        d = Date(4, 16, year)   # Get new year
        print('Current date is', d)
        s = d.dow()        # Get day of week
        dowd[s] += 1       # Count it

    print('Totals are', dowd)

# no problem with processing because my dow() method is different
# totals are {'Sunday': 630, 'Monday': 627, 'Tuesday': 630, 'Wednesday': 628, 'Thursday': 628, 'Friday': 630, 'Saturday': 627}
# so sunday, tuesday, and friday are the most common
# monday and saturday are the least
def commondow():
    """what are the most common days of the week?
    (specifically what day does the 13th of every month fall on for the next 400 years)"""

    dowd = {}              # dowd == 'day of week dictionary'
    dowd["Sunday"] = 0     # a 0 entry for Sunday
    dowd["Monday"] = 0     # and so on...
    dowd["Tuesday"] = 0
    dowd["Wednesday"] = 0
    dowd["Thursday"] = 0
    dowd["Friday"] = 0
    dowd["Saturday"] = 0

    # Live for another 100 years...
    for year in range(2021, 2421):
        for month in range(1, 12):
            d = Date(month, 13, year)   # Get new year
            print('Current date is', d)
            s = d.dow()        # Get day of week
            dowd[s] += 1       # Count it

    print('Totals are', dowd)
