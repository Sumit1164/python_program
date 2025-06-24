weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

BMI = weight / (height/100)**2
    
print(f"You BMI is: {BMI}")
    
if BMI < 18.5:
    print("You are underweight.")
elif 18.5 <= BMI < 24.9:
    print("You have a normal weight.")
elif 25 <= BMI < 29.9:
    print("You are overweight.")
else:
    print ("You are obese.")