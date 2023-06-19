# Ken Ka 1968133

#Output Menu

print("Davy's auto shop services")
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12\n')


#Customer picks two services
first_s = input('Select first service:\n')
second_s =  input('Select second service:\n')


#Output invoice
total = 0

print("\nDavy's auto shop invoice\n")
if first_s == ('Oil change'):
    print('Service 1: Oil change, $35')
    total += 35
elif first_s == ('Tire rotation'):
    print('Service 1: Tire rotation, $19')
    total += 19
elif first_s == ('Car wash'):
    print('Service 1: Car wash, $7')
    total += 7
elif first_s == ('Car wax'):
    print('Service 1: Car wax $12')
    total += 12
else:
    print('Service 1: No service')

if second_s == ('Oil change'):
    print('Service 2: Oil change, $35')
    total += 35
elif second_s == ('Tire rotation'):
    print('Service 2: Tire rotation, $19')
    total += 19
elif second_s == ('Car wash'):
    print('Service 2: Car wash, $7')
    total += 7
elif second_s == ('Car wax'):
    print('Service 2: Car wax, $12')
    total += 12
else:
    print('Service 2: No service')

print('\nTotal:','$',total)