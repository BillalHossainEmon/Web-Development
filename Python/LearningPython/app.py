weight = float(input("Please enter your weight: "))
print(weight)
unit = input("(K)gs or (L)bs: ")
if unit.upper() == "K":
    converted = weight/0.45
    print("Weight in Lb: " + str(converted))
else:
    converted = weight*0.45
    print("Weight in Kgs: " + str(converted))