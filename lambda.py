myLambda = lambda x : x * x
result = myLambda(2)
print(result)

#you can pass a lambda to the map function too
result = map((lambda  x : x * x ), [1,2,3] )
for item in result :
    print(item)