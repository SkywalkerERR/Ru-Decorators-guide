def header(func):

    def inner(*args,**kwargs): # Сначала say вернет значение данной функции
        print('<h1>')
        func(*args,**kwargs)
        print('</h1>')

    return inner

def table(func): # Далее результат из header пройдет сюда и вернет результат окончательный

    def inner(*args,**kwargs):
        print('<table>')
        func(*args,**kwargs)
        print('</table>')

    return inner
@table
@header # say = header(say)
def say(name,surname,age):
    print('hello',name,surname,age)

say('Vasya','Pupkin',30)