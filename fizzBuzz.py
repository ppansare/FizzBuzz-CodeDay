#Using the range 
for num in range(1, 101):
#check if it's divisible by 3 
  if num % 3 == 0:
    print("fizz")
#check if it's divisible by 5
  elif num % 5 == 0:
    print("buzz")
#check if they both are divisible. 
  elif num % 5 == 0 or num % 3 == 0:
    print("fizzbuzz")
  else:
    print(num)
