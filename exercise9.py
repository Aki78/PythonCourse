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
      print("Too fast")
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

    print(h)
    h += 1

print_properties(car_list)
    
