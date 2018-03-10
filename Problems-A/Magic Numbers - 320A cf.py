number = input()
length = len(number)
num = int(number)
magic = True
position = 0

while num!=0:
    a = num%10
    num = num//10

    if a==1:
        position = 0
    elif a==4 and position<2:
        position = position+1
    else:
        magic = False

if position!=0:
    magic = False

if magic == True:
    print("YES")
else:
    print("NO")


# Sample Input: 114114  Output: YES
# Sample Input: 1111  Output: YES
# Sample Input: 441231  Output: NO
