#1

class Elevator:
  def __init__(self):
      self.floor = 0

  def floor_up(self):
      self.floor += 1

  def floor_down(self):
      self.floor -= 1

  def go_to_floor(self,f):
      while 1:
          if self.floor > f:
              self.floor_down()
          elif self.floor < f:
              self.floor_up()
          else:
              break

e = Elevator()

e.go_to_floor(5)
print(e.floor)
e.go_to_floor(0)
print(e.floor)

#2,3
class Building:
    def __init__(self, n):
        self.elevators = []
        for i in range(n):
            self.elevators.append(Elevator())
    def run_elevator(self, el_num, f):
        self.elevators[el_num].go_to_floor(f)

    def fire_alarm(self):
        for _i in self.elevators:
            _i.go_to_floor(0)
        
b = Building(100)

b.run_elevator(50, 120)
print(b.elevators[50].floor)

b.fire_alarm()
print(b.elevators[50].floor)

        
# 4 -----> Go To Exercise9.py 
