import time
from threading import Thread
from time import sleep
class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.army = 100
        self.days = 0

    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.power > 0:
            #time.sleep(1)
            self.days += 1
            self.power -= 1
            self.army -= 1
            print(f"{self.name} сражается {self.days} день(дня), осталось {self.army}"
                  f"воинов, против {self.power} в армии врага")
            if self.army < 0:
                print(f"{self.name} Проиграл спустя {self.days} дней(дня)!")
                break
        if self.army == self.power:
            print(f"{self.name} Ничья спустя {self.days} дней(дня)!")
        elif self.army > self.power:
            print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")
        #print("Все битвы закончились!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")