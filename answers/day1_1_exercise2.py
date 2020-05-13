import math

list1 = [1, 2, 3, 4, 5, 6]
avg = sum(list1)/len(list1)
var = 0.0
for i in list1:
    var += (i - avg)**2
var /= len(list1)
sd = math.sqrt(var)
print("list = ", list1)
print("sd = %f" % sd)

