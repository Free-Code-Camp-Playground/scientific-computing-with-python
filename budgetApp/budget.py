class Category:
  def __init__(self, category):
    self.balance=0
    self.category = category
    self.ledger=[]

  def deposit(self, amount, description=""):
    self.balance += amount
    self.ledger.append({"amount": float(amount),
                        "description" :description})


  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.balance -= amount
      self.ledger.append({"amount": float(-amount),
                        "description" :description})
      return True
    return False

  def get_balance(self):
    return self.balance

  def transfer(self, amount, otherBudget):
    if self.check_funds(amount):
      desc = f"Transfer to {otherBudget.category}"
      self.withdraw(amount, desc)

      desc = f"Transfer from {self.category}"
      otherBudget.deposit(amount, desc)
      
      return True
    return False


  def check_funds(self, amount):
    return self.balance >= amount

  def __str__(self) -> str:
    prt = ""
    prt += f"{self.category:*^30}\n"
    for op in self.ledger:
      amount=op["amount"]
      desc=op["description"]
      if len(desc) > 23:
        prt += f"{desc:<.23s}{amount:>7.2f}\n"
      else:
        prt += f"{desc:<23s}{amount:>7.2f}\n"
    prt += f"Total: {self.balance}"
    return prt

def create_spend_chart(categories):
  spend={}
  totalSpend = 0
  catSizes=[]
  out=""
  for cat in categories:
    catSizes.append(len(cat.category))
    if cat.category not in spend.keys():
      spend[cat.category]=0
    
    for op in cat.ledger:
      if op["amount"] < 0:
        spend[cat.category] += op["amount"]
        totalSpend += op["amount"]
    
  out+="Percentage spent by category\n"
  for p in range(100, -10, -10):
    line = ""
    line += f"{p:>3d}|"
    for cat in categories:
      perct = 100*spend[cat.category]/totalSpend
      if perct > p:
        line += " o "
      else:
        line += "   "
    out+= line+" \n"
  out+="    "+"---"*len(categories)+"-\n"
  for c in range(max(catSizes)):
    line = "    "
    for cat in categories:
      if len(cat.category) > c:
        line += f" {cat.category[c]} "
      else:
        line += "   "
    out+=line+" \n"
  return out[:-1]


def main():
  food1 = Category("Food")
  food1.deposit(1000, "initial deposit")
  food1.withdraw(10.15, "groceries")
  food1.withdraw(15.89, "restaurant and more food for dessert")
  print(food1.get_balance())
  clothing = Category("Clothing")
  food1.transfer(50, clothing)
  clothing.withdraw(25.55)
  clothing.withdraw(100)
  auto = Category("Auto")
  auto.deposit(1000, "initial deposit")
  auto.withdraw(15)

  food=Category("Food")
  entertainment=Category("Entertainment")
  business=Category("Business")
  food.deposit(900, "deposit")
  entertainment.deposit(900, "deposit")
  business.deposit(900, "deposit")
  food.withdraw(105.55)
  entertainment.withdraw(33.40)
  business.withdraw(10.99)
  actual = create_spend_chart([business, food, entertainment])
  expected = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "

  print(actual.replace(" ","*"))
  print(expected.replace(" ","*"))

  print(food1)
  print(clothing)

  print(create_spend_chart([food1, clothing, auto]))

if __name__ == "__main__":
  main()