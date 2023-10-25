#linear
list = [1,2,3,4,5]
print(list)
x = int(input("enter key: "))

for i in list:
    if i == x:
        print(list.index(i))

#binary

low = 0
high = len(list) - 1

while(low <= high):
    mid = (low + high) // 2
    if(list[mid] == x):
        print(mid)
        break
    elif(list[mid] > x):
        high = mid - 1
    else:
        low = mid + 1
