# # -*- coding: utf-8 -*-
class TrainCar(object):
    def __init__(self, color_type=None, passenger_list=[]):
        self.color_type = color_type
        self.passenger_list = passenger_list


class Train(object):
    def __init__(self):
        self.cars = []

    @property
    def passenger_count(self):
        return sum([len(car.passenger_list) for car in self.cars])


if __name__=="__main__":
    train = Train()
    for i in range(0, 10):
        train_car = TrainCar(color_type="keiyo")
        train_car.passenger_list.append("Taro Yamada")
        train.cars.append(train_car)

    print(train.passenger_count)