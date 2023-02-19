def synthesis(inputs, outputs):

    operations = ["+", "-", "*", "/"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    ans = []
    for n in numbers:
      for op in operations:
        if op == "+":
          newVal = inputs + int(n)
        elif op == "-":
          newVal = inputs - int(n)
        elif op == "*":
          newVal = inputs * int(n)
        elif op == "/":
          if inputs % int(n) == 0:
            newVal = inputs // int(n)
          else:  # if odd, skip
            continue
        if eval(str(inputs)+op+str(newVal)) == outputs:
          ans.append(op+str(newVal))
    print(ans)


synthesis(2, 6)
synthesis(2, 2)
synthesis(7, 2)
