
def error(msg):
    err = f'Error: {msg}'
    return err

def convert_12h_format(time):
  clock, part = time.split()
  h, m=list(map(int, clock.split(":")))
  if part=="PM":
    h = int(h)+12
    return f"{h}:{m:02d}"
  return f"{h}:{m:02d}"

def convert_24h_format(time):
  h, m=list(map(int, time.split(":")))
  if int(h) == 12:
    return f"{h}:{m:02d} PM"
  elif int(h) == 0:
    h = 12
    return f"{h}:{m:02d} AM"
  elif int(h) > 12:
    h = int(h)-12
    return f"{h}:{m:02d} PM"
  return f"{h}:{m:02d} AM"

def count_days(time):
  days=0
  if time[0] >= 24:
    days = time[0]//24
    time[0] -= 24*days
  return time, days

def eval_week(week, addDays):
  weekDays=["monday",
            "tuesday",
            "wednesday",
            "thursday",
            "friday",
            "saturday",
            "sunday"]
  currWeekDay = weekDays.index(week.lower())
  nextWeekDay = currWeekDay + addDays
  return weekDays[nextWeekDay % len(weekDays)]
  
  

def add_time(start, duration, week=None):
  startTime = list(map(int, convert_12h_format(start).split(":")))

  addTime = list(map(int, duration.split(":")))
  addTime, addDays = count_days(addTime)

  finalTime = [(startTime[0]+addTime[0]), 
               (startTime[1]+addTime[1])]
  if finalTime[1]>=60:
    finalTime = [finalTime[0]+1, finalTime[1]-60]
  finalTime, newDay = count_days(finalTime)

  new_time = convert_24h_format(f"{finalTime[0]}:{finalTime[1]:02d}")
  passedDays = addDays + newDay

  if week:
    currWeek = eval_week(week, passedDays)
    new_time += f", {currWeek.capitalize()}"

  if passedDays == 1:
    new_time += f" (next day)"
  elif passedDays > 1:
    new_time += f" ({passedDays} days later)"

  return new_time


def main():
  # print(convert_12h_format("3:00 PM"))
  # print(add_time("3:00 PM", "3:10"))
  # print(add_time("11:30 AM", "2:32", "Monday"))
  print(add_time("11:45 AM", "00:20"))
  print(add_time("11:59 PM", "24:05", "Wednesday"))
  # print(add_time("10:10 PM", "3:30"))
  # print(add_time("11:43 PM", "24:20", "tueSday"))
  # print(add_time("6:30 PM", "205:12"))

if __name__ == "__main__":
  main()