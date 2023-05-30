weight = float(input("Your weight: "))
metric = str(input("(K)g or (L)bs: "))

if metric.upper() == "L":
    converted_weight = weight / 2.20462
    print("Weight in Kg: " + str(converted_weight))
else:
    converted_weight = weight * 2.20462
    print("Weight in Lbs: " + str(converted_weight))