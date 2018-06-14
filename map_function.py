def my_function(num):
    return num * num

my_array  = [1,2,3]


my_list = map(my_function, my_array)
#point to note
#map returns/or can be cast to list
#point to note : you just pass the function name, not invoke the function.

#applies the square function on all the iterators
for item in my_list:
    print (item)

