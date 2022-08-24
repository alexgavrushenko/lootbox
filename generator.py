import random

names = {
    "Alex": 4,
    "Alexey": 7,
    "Marios": 10,
    "Sergey": 12,
    "Ihor": 15,
    "Petros": 17,
    "Victor": 20,
}

resources = {
    "wood": 1000,
    "silver": 100,
    "gold": 20,
    "platinum": 5,
    "etherium": 2
}

time = 1661356911

total = {}

for i in range(100000):
    time = time + random.randint(1,5)
    name = random.choices(list(names.keys()), list(names.values()))[0]
    resource = random.choices(list(resources.keys()), list(resources.values()))[0]
    value = random.randint(-int(resources[resource]/2), resources[resource])
    
    if name not in total:
        total[name] = {}
    if resource not in total[name]:
        total[name][resource] = 0
        
    if -value > total[name][resource]:
        value = -total[name][resource]

    if(random.random() > 0.99):
        value = -total[name][resource]

    if value == 0:
        value = 1
    
    total[name][resource] = total[name][resource] + value
    
    print({
        'timestamp': time,
        'name': name,
        'resource': resource,
        'value': value
    })