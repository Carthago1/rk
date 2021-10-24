from operator import itemgetter
from driver import Driver
from carpark import CarPark
from drivercarpark import DrCarPark

drivers = [
    Driver(1, 'Петров', 25000, 1),
    Driver(2, 'Иванов', 27000, 2),
    Driver(3, 'Сидоров', 30000, 3),
    Driver(4, 'Михайлов', 24000, 3),
    Driver(5, 'Базаров', 31000, 1)]

car_parks = [
    CarPark(1, 'Автопарк №1'),
    CarPark(2, 'Автопарк №2'),
    CarPark(3, 'Автопарк №3'),   
    CarPark(11, 'Парк №1'),
    CarPark(22, 'Парк №2'),
    CarPark(33, 'Парк №3')]
 
dr_car_park = [
    DrCarPark(1,1),
    DrCarPark(2,2),
    DrCarPark(3,3),
    DrCarPark(2,4),
    DrCarPark(3,5),
 
    DrCarPark(11,1),
    DrCarPark(22,2),
    DrCarPark(33,3),
    DrCarPark(22,4),
    DrCarPark(33,5)]
 
def main():
    one_to_many = [(dr.fio, dr.sal, c_p.name) 
        for c_p in car_parks 
        for dr in drivers 
        if dr.car_park_id == c_p.id]
    
    many_to_many_temp = [(c_p.name, d_c_p.car_park_id, d_c_p.driver_id) 
        for c_p in car_parks 
        for d_c_p in dr_car_park 
        if c_p.id == d_c_p.car_park_id]
    
    many_to_many = [(dr.fio, dr.sal, c_p_name) 
        for c_p_name, car_park_id, driver_id in many_to_many_temp
        for dr in drivers if dr.id == driver_id]
 
    print('Задание Г1')
    res_11 = [(c_p.name,
              list(fio for fio, _, name in one_to_many if name == c_p.name))
              for c_p in car_parks if c_p.name[0] == 'А']
    print(res_11) 
    
    print('\nЗадание Г2')
    res_12_unsorted = []
    for c_p in car_parks:
        c_p_drivers = list(filter(lambda x: x[2] == c_p.name, one_to_many))
        if len(c_p_drivers) > 0:
            res_12_unsorted.append(
                (c_p.name, max(c_p_drivers, key = lambda x: x[1])[1]))
 
    res_12 = sorted(res_12_unsorted, key = itemgetter(1), reverse = True)
    print(res_12)
 
    print('\nЗадание Г3')
    res_13 = []
    for fio, _, c_p_name in many_to_many:
        res_13.append((fio, c_p_name))
    res_13 = sorted(res_13, key = itemgetter(1))
    print(res_13)
 
if __name__ == '__main__':
    main()
