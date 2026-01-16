num=7
if num%2==0:
    print("even")
else:
    print("odd")
marks=int(input())
if marks>=90:
    print("Grade A")
elif marks>=80:
    print("Grade B")
else:
    print("Grade C")


for i in range(1,6):
    print(i)


j=1
while j<=10:
    print(j)
    if j==2:
        break
    j+=1

day =4
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("Friday")
