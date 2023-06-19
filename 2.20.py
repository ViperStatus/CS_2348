# Ken Ka 1968133

lem_juice = float(input('Enter amount of lemon juice (in cups):\n'))
water = float(input('Enter amount of water (in cups):\n'))
aga_nec = float(input('Enter amount of agave nectar (in cups):\n'))
serv = float(input('How many servings does this make?\n'))

print('\nLemonade ingredients - yields', '{:.2f}'.format(serv), 'servings')
print('{:.2f}'.format(lem_juice), 'cup(s) lemon juice')
print('{:.2f}'.format(water), 'cup(s) water')
print('{:.2f}'.format(aga_nec), 'cup(s) agave nectar')

want_serv = float(input('\nHow many servings would you like to make?\n'))



print('\nLemonade ingredients - yields', '{:.2f}'.format(want_serv), 'servings')
print('{:.2f}'.format(lem_juice*want_serv/serv), 'cup(s) lemon juice')
print('{:.2f}'.format(water*want_serv/serv), 'cup(s) water')
print('{:.2f}'.format(aga_nec*want_serv/serv), 'cup(s) agave nectar')

print('\nLemonade ingredients - yields', '{:.2f}'.format(want_serv), 'servings')
print('{:.2f}'.format(lem_juice*want_serv/serv/16), 'gallon(s) lemon juice')
print('{:.2f}'.format(water*want_serv/serv/16), 'gallon(s) water')
print('{:.2f}'.format(aga_nec*want_serv/serv/16), 'gallon(s) agave nectar')