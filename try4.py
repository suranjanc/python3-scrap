import datetime

dateEntered='13 Sep 2020'

print(datetime.datetime.strptime(dateEntered,'%d %b %Y').weekday())