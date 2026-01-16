sub=lambda a,b:a-b
print(sub(10,20))

multi=lambda c,d:c*d
print(multi(100,20))

maximum=lambda x,y:x if x>y else y
print(maximum(10,20))

min=lambda x,y:x if x<y else y
print(min(10,6))


numbers=[1,2,3,4,5]
result=map(lambda x:x*2,numbers)
print(list(result))
