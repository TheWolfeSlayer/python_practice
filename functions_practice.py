def hello():
    print('greetings User')

def pack(x, y, z):
    return [x, y, z]

def eat_lunch(lunchbox):
    if len(lunchbox) > 0:
        for ii in range(len(lunchbox)):
            if ii == 0:
                print(f'First I eat {lunchbox[0]}')
            else:
                print(f'Next I eat {lunchbox[ii]}')
        print('My lunchbox is now empty')
    else:
        print('My lunchbox is empty')
 

food=['Apple', 'Toast', 'Oreos']

hello()

print(pack(3, 'Math', True))

eat_lunch(food)
