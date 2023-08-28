import copy
import random

class Hat:
  def __init__(self, **kwargs):
    self.contents=[]
    for b in kwargs:
      for ball in range(kwargs[b]):
        self.contents.append(b)

  def draw(self, quantity):
    if quantity > len(self.contents):
      return copy.copy(self.contents)

    drewBalls=[]
    for ball in range(quantity):
      randomPos = random.randint(0, len(self.contents)-1)
      drewBalls.append(self.contents.pop(randomPos))
    
    return drewBalls
    
def check_run(run, expected_run):
  for ball in expected_run:
    try:
      run.remove(ball)
    except ValueError:
      return False
  return True


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  expected_run=[]
  correct_run=0
  for b in expected_balls:
    for ball in range(expected_balls[b]):
      expected_run.append(b)
  
  for run in range(num_experiments):
    testHat=copy.deepcopy(hat)
    drewBalls=testHat.draw(num_balls_drawn)
    if check_run(drewBalls, expected_run):
      correct_run+=1

  return correct_run/num_experiments


def main():
  hat1 = Hat(yellow=3, blue=2, green=6)
  hat2 = Hat(red=5, orange=4)
  hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)

  hat = Hat(black=6, red=4, green=3)
  probability = experiment(hat=hat,
                    expected_balls={"red":2,"green":1},
                    num_balls_drawn=5,
                    num_experiments=2000)

  print(probability)


if __name__ == "__main__":
  main()