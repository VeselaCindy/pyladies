# 1
"""
pets = {
    'Willie': 'cat',
    'Ronny': 'dog',
    'Joe': 'squirrel'
}


for name, pet in pets.items():
    print('{} is a {}'.format(name, pet))

"""

# 2
pets = {
    'Willie': 'cat',
    'Ronny': 'dog',
    'Joe': 'squirrel'
}


for name, pet in pets.items():
    print(name, 'is a', pet)
    # pets.update({'John':'rat'}) 

for name, pet in pets.items():
    print(name, 'is a', pet)
    # del pets[name]