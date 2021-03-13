import datetime
nextSetOFDate = {}

weekDays = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
short_week_days = dict(mo="Mon", tu="Tue", we="Wed", th="Thu", fr="Fri", sa="Sat",
                       su="Sun")
#
# NextDay1 = datetime.datetime.today() + datetime.timedelta(days=3)
# NextDay_Date_Formatted = NextDay1.strftime('%d %b')  # format the date to ddmonth
# print(str(weekDays[NextDay1.weekday() - 1] +' '+ NextDay_Date_Formatted))
# nextSetOFDate[weekDays[NextDay1.weekday() - 1]] = NextDay_Date_Formatted
#
# NextDay2 = datetime.datetime.today() + datetime.timedelta(days=4)
# NextDay_Date_Formatted = NextDay2.strftime('%d %b')  # format the date to ddmonth
# print(str(weekDays[NextDay2.weekday() - 1] +' '+ NextDay_Date_Formatted))
# nextSetOFDate[weekDays[NextDay2.weekday() - 1]] = NextDay_Date_Formatted
#
# NextDay3 = datetime.datetime.today() + datetime.timedelta(days=5)
# NextDay_Date_Formatted = NextDay3.strftime('%d %b')  # format the date to ddmonth
# print(str(weekDays[NextDay3.weekday() - 1] +' '+ NextDay_Date_Formatted))
# nextSetOFDate[weekDays[NextDay3.weekday() - 1]] = NextDay_Date_Formatted
#
# NextDay4 = datetime.datetime.today() + datetime.timedelta(days=6)
# NextDay_Date_Formatted = NextDay4.strftime('%d %b')  # format the date to ddmonth
# print(str(weekDays[NextDay4.weekday() - 1] +' '+ NextDay_Date_Formatted))
# nextSetOFDate[weekDays[NextDay4.weekday() - 1]] = NextDay_Date_Formatted
#
#
# NextDay5 = datetime.datetime.today() + datetime.timedelta(days=7)
# NextDay_Date_Formatted = NextDay5.strftime('%d %b')  # format the date to ddmonth
# print(str(weekDays[NextDay5.weekday() - 1] +' '+ NextDay_Date_Formatted))
# nextSetOFDate[weekDays[NextDay5.weekday() - 1]] = NextDay_Date_Formatted
#
# print(nextSetOFDate)
#
# nextSetOFDate = {}

Today = datetime.datetime.today()
nextSetOFDate[weekDays[Today.weekday()]] = 'Today'

Tomorrow = datetime.datetime.today() + datetime.timedelta(days=2)
nextSetOFDate[weekDays[Tomorrow.weekday()-1]] = 'Tomorrow'

for num in range(3 , 8):
    NextDay = datetime.datetime.today() + datetime.timedelta(days=num)
    nextSetOFDate[weekDays[NextDay.weekday() - 1]] = str(weekDays[NextDay.weekday() - 1] + ' ' + NextDay.strftime('%d %b'))

print(nextSetOFDate)


print( list(nextSetOFDate.values()).index('Fri 30 Jan'))
print(nextSetOFDate.keys())