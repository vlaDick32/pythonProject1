import logging
import random

class Pet:
    def __init__(self, name="Pet"):
        self.name = name
        self.gladness = 50
        self.satiety = 50
        self.stamina = 50
     def chill(self):
        self.gladness += 10
        self.stamina +=20


    def eat(self):
     if self.bowl.food <= 0:
     else:
        if self.satiety >= 100:
            self.satiety = 100
            return
        self.satiety += 5
        self.bowl.food -= 5
     def walk(self):
       gladnes = +20
       stamina = -20

















       def days_indexes(self, day):
           day = f" Today the {day} of {self.name}'s life "
           print(f"{day:=^50}", "\n")
           human_indexes = self.name + "'s indexes"
           print(f"{human_indexes:^50}", "\n")
           print(f"Money – {self.money}")
           print(f"Satiety – {self.satiety}")
           print(f"Gladness – {self.gladness}")
           home_indexes = "Home indexes"
           print(f"{home_indexes:^50}", "\n")
           print(f"Food – {self.home.food}")
           print(f"Mess – {self.home.mess}")
           car_indexes = f"{self.car.brand} car indexes"
           print(f"{car_indexes:^50}", "\n")
           print(f"Fuel – {self.car.fuel}")
           print(f"Strength – {self.car.strength}")

       def is_alive(self):
           if self.gladness < 0:
               print("Depression…")
               return False
           if self.satiety < 0:
               print("Dead…")
               return False
           if self.money < -500:
               print("Bankrupt…")
               return False

       def live(self, day):
           if self.is_alive() == False:
               return False
           if self.home is None:
               print("Settled in the house")
               self.get_home()
           if self.car is None:
               self.get_car()
               print(f"I bought a car{self.car.brand}")
           if self.job is None:
               self.get_job()
               print(f"I don't have a job, I'm going to get a job "
                     f"{self.job.job} with salary {self.job.salary}")
           self.days_indexes(day)
           dice = random.randint(1, 4)
           if self.satiety < 20:
               print("I'll go eat")
               self.eat()
           elif self.gladness < 20:
               else:
                   print("Let`s chill!")
                   self.chill()

