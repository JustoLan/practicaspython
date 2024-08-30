weight = int(input ("Weight: "))
unit = input("(K)g or (L)bs: ")

if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in kg: " + str(converted))

numbers = [1,2,3,4,5]
numbers.remove(4,2)