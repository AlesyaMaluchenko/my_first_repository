class Base:
    def get(self):
        return self._x, self._y #функция создаёт своё пространство имён, вместо self можно и другую букву
    def set(self, x, y):
        self._x = x
        self._y = y
    def __init__(self, x, y): # можно по умолчанию ввести x=0, y=0
        self.set(x, y)

a = Base(4, 7) #внутри а теперь лежат две переменные
b = Base(0, 0)
c = Base()
b._x = 5
b._y = 7
print(a._x, a._y) #вызываем
print(b._x, b._y)
print(*a.get()) # обращаемся к get и подтягиваем a к get, вместо self подставляется a
print(*b.get())
a.set(4, 6)
print(*a.get())


