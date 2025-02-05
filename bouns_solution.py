# Bonus

print("Welcome to mass body calculater")
print("*"*35)
height:float=float(input("Please Enter Your Height : "))
wieght:float=float(input("Please Enter Your wieght : "))

bmi= wieght/(height/100)**2
print(bmi)

if bmi<=18.5:
    print("You are underweight. Watch your health")
elif bmi >18.5 and bmi <24.9:
    print("You are fit & healthy")
else:
    print("You are overwieght you need to work out more and watch your diet")
