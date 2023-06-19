# Ken Ka 1968133

import math

# User Input
wall_h = int(input('Enter wall height (feet):\n'))
wall_w = int(input('Enter wall width (feet):\n'))
# Wall Area Calculation
wall_a = wall_w*wall_h

print('Wall area:', wall_a, 'square feet')
print('Paint needed:', '{:.2f}'.format(wall_a/350), 'gallons')
can = math.ceil(wall_a/350)
print('Cans needed:',can, 'can(s)\n')

color_dict = {'red':35,'blue':25,'green':23}
color = input('Choose a color to paint the wall:\n')
print('Cost of purchasing', color, 'paint: $' +str(can*color_dict[color]))