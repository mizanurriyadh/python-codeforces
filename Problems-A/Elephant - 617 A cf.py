distance = input()
d = int(distance)
if d<=5:
    print('1')
else:
    if d%5==0:
        res = d//5
        print(res)
    else:
        res = (d//5)+1
        print(res)


# Sample Input:999998  Output:200000
# Sample Input:999995  Output:199999
# Sample Input:86380  Output:17276
# Sample Input:94190  Output:18838
