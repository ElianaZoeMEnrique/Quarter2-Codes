sum = 0
age = int(input("Hi there! Please enter your age: "))

for x in range (1, age + 1):
    sum += x

print("The sum of all numbers from 1 to", age, "is:", sum)