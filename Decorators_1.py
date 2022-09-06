def decorator(func):

    def inner(n):
        print('start decorator....')
        func(n) #функция say
        print('end decorator....')

    return inner

def say(name):
    print('hello',name)

say = decorator(say)
say('Vasya')