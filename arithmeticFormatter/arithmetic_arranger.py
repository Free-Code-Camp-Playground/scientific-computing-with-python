def error(msg):
    err = f'Error: {msg}'
    return err

def check_operation(n1, op, n2):
  err = ""
  if op not in ["+", "-"]:
    err = error("Operator must be '+' or '-'.")
    return True, err
  if not n1.isdigit() or not n2.isdigit():
    err = error("Numbers must only contain digits.")
    return True, err
  if len(n1)>4 or len(n2)>4:
    err = error("Numbers cannot be more than four digits.")
    return True, err
  return False, err

def arithmetic_arranger(operations, solve=False):
  if len(operations)>5:
    return "Error: Too many problems."
  l1, l2, l3, l4 = "", "", "", ""
  for operation in operations:
    n1, op, n2 = operation.split()
    check, err = check_operation(n1, op, n2)
    if check: 
      return err
    space = max(len(n1), len(n2))
    l1+=f"  {n1:>{space}}    "
    l2+=f"{op} {n2:>{space}}    "
    l3+="-"*(space+2)+"    "
    l4+=f"{eval(operation):>{space+2}}    "
  arranged_problems = l1[:-4]+"\n"+l2[:-4]+"\n"+l3[:-4]
  if solve:
    arranged_problems+="\n"+l4[:-4]
  return arranged_problems

def main():
  print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
  print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))

if __name__ == "__main__":
  main()