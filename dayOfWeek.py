import datetime
import calendar

#func to get input date
def getDate():
    inputDate=str(input("Enter the date, month, year: ").strip())
    return inputDate

#func to check day of week
def checkDayOfWeek(inputDate):
    dateObj=datetime.datetime.strptime(inputDate, '%d, %b, %Y').weekday()
    dayOfW=calendar.day_name[dateObj]
    return dayOfW

#Main
print(checkDayOfWeek(getDate()))