class Car:
    _car_count = 0 # это поле, int неизменяем, если будет [], то он будет изменяться и остальные экземпляры тоже

    def __init__(self, name):
        self._name = name
        Car._car_count += 1
    def get_number_of_cars(self):
        return self._car_count
a = Car("Lada")
b = Car("Gas")
c = Car("Tesla")

print(c.get_number_of_cars()) #если написать b или a, то всё равно будет 3



