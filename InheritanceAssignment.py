


class Guitar: #This creates a parent class of guitar
    brand = 'No Brand Provided'
    model = ' '
    color = ' '
    year = ' '


# This is a specific type of guitar that has many of
#of the same attributes of all guitars but is unique
# in it's operation

class Electric(Guitar): 
    pickups = ' '
    switch = ' '

# This is a specific type of guitar that has many of
#of the same attributes of all guitars but is unique
#in it's operation    

class Acoustic(Guitar):
    style = ' '
    tonewood = ' '
    acoustic/electric = ' '
