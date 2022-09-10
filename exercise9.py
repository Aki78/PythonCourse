import random
#1,2,3

class Car:
  def __init__(self, registration, max_speed):
    self.registration = registration
    self.max_speed = max_speed
    self.current_speed = 0
    self.distance = 0
  def accelerate(self, add_speed):
    speed = self.current_speed + add_speed 
    if self.max_speed > speed and speed > 0 :
      self.current_speed += add_speed
    elif speed < 0:
        self.current_speed = 0
    else:
        pass
      # print("Too fast")
  def run(self, h):
      self.distance += self.current_speed*h

c1 = Car("ABC-123", 142)

print(c1.registration)
print(c1.max_speed)
print(c1.current_speed)
print(c1.distance)

c1.accelerate(+30)
c1.accelerate(+70)
c1.accelerate(+50)
c1.accelerate(-200)

print(c1.current_speed)

c1.accelerate(60)
c1.distance = 2000
c1.run(1.5)

print(c1.distance)

# 4

def update_speed(car_list):
    for _i in car_list:
        _i.accelerate(random.randint(-10,15))
        _i.run(1)

def print_properties(car_list):
    for _i in car_list:
        print(_i.distance, _i.current_speed)

def check_if_goal(car_list):
    for _i in car_list:
        if _i.distance > 10000:
            return True
    return False

car_list = []
for i in range(10):
    car_list.append(Car("ABC-" + str(i+1), random.randint(0,100)))
h = 0
while 1:
    if  check_if_goal(car_list):
        break
    update_speed(car_list)

    # print(h)
    h += 1

print_properties(car_list)
    


# EXERSICE 10 Section 4

class Race:
    def __init__(self, race_name, race_km, car_list):
      self.race_name = race_name
      self.race_km = race_km
      self.car_list = car_list
    def hour_passes(self):
        update_speed(self.car_list)
        for _i in self.car_list:
            _i.run(1)

    def race_finished(self):
        for _i in self.car_list:
            if _i.distance < self.race_km:
                return False
        return True

    def __repr__(self):
        text = "speed (km/h) |  distance (km)\n"
        for _i in self.car_list:
            text += str(_i.current_speed) + "km/h | " + str(_i.distance) + "km\n"
        return text

r = Race("Grand Demolition Derby",10000,car_list)
print("Starting race")
for i in range(100000):
    print(i)
    if  r.race_finished():
        break
    r.hour_passes()

    if i%10 == 0:
        print(r)


# EXERSICE 11 Section 2
class ElectricCar(Car):
  def __init__(self, registration, max_speed, capacity):
    self.capacity = capacity
    super().__init__(registration, max_speed)

  def print_info(self):
      print(self.registration, "", self.current_speed, "", self.capacity, "kwh",self.distance, "km")

class StinkyCar(Car):
  def __init__(self, registration, max_speed, tank):
    self.tank = tank
    super().__init__(registration, max_speed)

  def print_info(self):
      print(self.registration, "", self.current_speed, "", self.tank, "liters", self.distance, "km")

e = ElectricCar("ABC-15", 180, 52.5)
s = StinkyCar("ABC-15", 165, 32.3)

e.current_speed = 150
s.current_speed = 120

for i in range(10):
    e.run(1)
    s.run(1)

e.print_info()
s.print_info()



