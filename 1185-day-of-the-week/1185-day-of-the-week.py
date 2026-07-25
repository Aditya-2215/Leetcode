class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        week = ["Monday", "Tuesday", "Wednesday","Thursday", "Friday", "Saturday", "Sunday"]
        daysInMonths = [31, 28, 31, 30, 31, 30,31, 31, 30, 31, 30, 31]
        totalDays = 0
        for y in range(1971, year):
            if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
                totalDays += 366
            else:
                totalDays += 365
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            daysInMonths[1] = 29
        for m in range(month - 1):
            totalDays += daysInMonths[m]
        totalDays += day - 1
        return week[(totalDays + 4) % 7]