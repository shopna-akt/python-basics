list = [1,2,3,4,5,6]
i = 0
while (i<=len(list)):
    if (list[i]==3):
        print ("found at index",i)
        break
    else:
        print("not found")
        i+=1

i = 0
while (i<=5):
    if (i==3):
        i+=1
        continue
    print (i)
    i+=1

i=0
while (i<=10):
    if (i%2 == 1):
        i+=1
        continue
    print (i)
    i+=1