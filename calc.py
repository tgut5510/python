# create calculator

# two number addition function
def add(x, z):
  return x + z

# two number subtraction function
def subtract(x, z):
  return x - z

# two number multiplication function
def multiply(x, z):
  return x * z

# two number division function
def divide(x, z):
  return x / z

# user selection
print("select operation")
print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")

while True:
# input from user
  choice = input("enter choice(1/2/3/4): ")

# test choice = 1 of 4 option
  if choice in ('1', '2', '3', '4'):
    num1 = float(input("enter first number: "))
    num2 = float(input("enter second number: "))

  if choice == '1':
    print(num1, '+', num2, '=', add(num1,num2))
  elif choice == '2':
    print(num1, '-', num2, '=', subtract(num1,num2))
  elif choice == '3':
    print(num1, '*', num2, '=', multiply(num1,num2))
  elif choice == '4':
    print(num1, '/', num2, '=', divide(num1,num2))
  else:
    print("invalid input")
