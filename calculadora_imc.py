print("CALCULADORA DE IMC")

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

weight2 = float(weight)
height2 = float(height)
bmi = weight2 / height2 ** 2
bmi = int(bmi)
print(bmi)
