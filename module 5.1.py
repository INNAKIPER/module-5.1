

# class House:
#     def __init__(self):
#         self.name='name'
#         self.numbers_of_floors='numbers_of_floors'
#     def go_to(self, new_floor):
#         self.new_floor='new_floor'
#             if new_floor <1 or > self.numbers_of_floor:

class House:
    def __init__(self, name, number_of_floors):
       self.name = name
       self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        floor = 0
        print(f'Здание {self.name} имеет {self.number_of_floors} этажей \Поднимаемся на {new_floor}-й этаж')
        if new_floor < 1 or new_floor > self.number_of_floors:
            print(f'Вы ввели не верный этаж {new_floor}, такого этажа не существует')
        else:
            for floor in range(new_floor):
                print(floor + 1)
            print(f'Этаж № {new_floor} мы прибыли на ваш этаж, выходите')


h1= House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

h1.go_to(5)
h2.go_to(10)






