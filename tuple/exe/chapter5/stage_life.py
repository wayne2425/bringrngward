age = input("enter your age:")
age = int(age)


if age < 2:
    print("you are a baby.")
elif age>=2 and age<4:
        print("you are a toddler.")
elif age >= 4 and age < 13:
      print("you are a kid.")
elif age >= 13 and age < 20:
      print("you are a teenager.")
elif age >=20 and age < 65:
      print("you are a adult.")
else:
      print("you are an elder.")