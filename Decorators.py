def decorator(func): #вместо func - передаем say

    def inner(): #inner - вложенная функция
        print('start decorator....')
        func() #функция say
        print('end decorator....')

    return inner

def say():
    print('hello world!')

say = decorator(say)
say() # Отрабатывает функция inner, печатает print1, функцию которую передали, print2

#Хочу расширить функционал say - за счет вызова функции decorator

