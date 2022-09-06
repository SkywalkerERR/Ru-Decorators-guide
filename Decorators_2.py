def header(func):

    def inner(*args,**kwargs): # Сначала say вернет значение данной функции
        print('<h1>')
        func(*args,**kwargs)
        print('</h1>')

    return inner

def say(name,surname,age):
    print('hello',name,surname,age)

def table(func): # Далее результат из header пройдет сюда и вернет результат окончательный

    def inner(*args,**kwargs):
        print('<table>')
        func(*args,**kwargs)
        print('</table>')

    return inner
say = header(table(say))
say('Vasya','Pupkin',30)