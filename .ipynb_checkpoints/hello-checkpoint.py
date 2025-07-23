def is_adult(age):
    if age >= 18:
        print('adult')
    else:
        print('minor')
is_adult(20)  # Call the function to see output

fruits = ["apples", "banana", "cheries"]
print(fruits[0])

print(help(fruits))
print(len(fruits))

fruits.append("pineapple")
fruits.sort()

fruits.count("banana")

for x in fruits: #fruits is the list and fruit is a variable that takes each value in the list one by one
    print(x)

total = 0
for i in range(1, 6):
    total += i  # same as total = total + i

print(total)  # Output: 15
