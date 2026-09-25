list = [1,3,2,5,8,4]
print (list)
print (list[3])
list[2]=7
print (list)

print(list[1:4])
print(list[:3])
print(list[2:])

list.append(9)
print(list)
list.sort()
print(list)
list.sort(reverse = True)
print (list)
list.reverse()
print(list)
list.insert(5,10)
print(list)
list.remove(8)
print(list)
list.pop(4)
print(list)