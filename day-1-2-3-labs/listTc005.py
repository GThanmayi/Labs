numbers=[10,20,30,40]
names=["thanu","nani","jyo"]
mixed=[1,"python",3.5,True]

numbers[1]=100
print(numbers)
print(names)
print(mixed)

for i in numbers:
    print(i)

if 10 in numbers:
    print("found")
else:
    print("not found")

matrix=[[1,2,3],[4,5,6]]
print(matrix[1][2])

names.reverse()
print(names)
names.append("kalki")
print(names)
names.remove("jyo")
print(names)
names.extend(["satya","vara"])
print(names)
names.insert(3,"int")
print(names)