# Ken Ka 1968133

print('Birthday Calender')

cur_m = int(input('Please enter the current month (number) '))
cur_d = int(input('Please enter the current day (number) '))
cur_y = int(input('Please enter the current year '))
user_m = int(input('Please enter the month you were born '))
user_d = int(input('Please enter the day you were born '))
user_y = int(input('Please enter the year you were born '))

print('Current day')
print('Month:', cur_m)
print('Day:', cur_d)
print('Year:', cur_y)

print('Birthday')
print('Month:', user_m)
print('Day:', user_d)
print('Year:', user_y)

years = cur_y - user_y - 1
if (user_m<cur_m):
    years += 1
elif (cur_m == user_m):
    if (user_d<cur_d):
        years += 1
if (cur_m == user_m and cur_d == user_d):
    print('Happy Birthday!')
print('You are ' +str(years)+' years old.')

