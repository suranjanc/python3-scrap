import datetime

#input date
dateEntered=datetime.datetime.strptime(str('13, '+ (input('Enter the month and year for which you find Friday/13: ').strip())),'%d, %b, %Y').weekday()
print(dateEntered)

if dateEntered==4:
    print("This month has Friday the 13th")
else:
    print("No Friday the 13th this month.")

#print(dateEntered)

#func to calc friday 13
#def isFriday13():

