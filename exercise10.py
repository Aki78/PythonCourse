import random
#1,2,3

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

