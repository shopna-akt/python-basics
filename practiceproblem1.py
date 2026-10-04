# palindrome of the list

list = ["M","A","D","A","M"]
if list == list[::-1]:
    print("It is palindrome")
else:
    print ("It is not palindrome")

#enter name of movies in a list
list = []
mov1 = input ("Enter the name:")
list.append(mov1)
mov2 = input ("Enter the name:")
list.append(mov2)
mov3 = input ("Enter the name:")
list.append(mov3)
print (list)


#Count tuple
tup = ("C","D","A","A","B","B","A")
print(tup.count("A"))

# print the given data in a dictionary
dictionary={
    "cat" :"a small animal",
    "table": [
        "a piece of furniture",
        "list of facts and figures"]
}
print (dictionary)


#given a list of subjects for students. Asssume 1 subject is required for 1 classroom.Count the classroom
sub= {"python" , "java" , "C++" , "python", "javascript", "java", "python" ,"java", "C++" , "C"}
print(sub)
classroom = len(sub)
print(classroom)


#enter marks of 3 subjects from the user and strore them in  dictionary
dictionary= {}
mark1 = int (input ("Enter the mark:"))
mark2 = int (input ("Enter the mark:"))
mark3 = int (input ("Enter the mark:"))
dictionary["Physics"]= mark1
dictionary["Chemistry"]= mark2
dictionary["Boilogy"]= mark3
print (dictionary)

#Figure out a way to store 9 & 9.0 as separate values in the set. 
values = {9, "9.0"}
print (values)

#print number from 1 to 100
num = 1
while (num <= 100):
    print (num)
    num+=1


#print the numbers from 100 to 1
num = 100
while (num>=1):
    print (num)
    num-=1

#print the multiplication table of number n
n = int (input ("Enter the num:"))
i =1
while (i <=10):
    print (f"{n}*{i}=",n*i)
    i+=1

#Print the elements of the following list using a loop. [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
list =[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
i = 0
while (i<10):
    print(list[i])
    i+=1

#Search for a number x in this tuple using loop
tup = (1,6,4,5,3,2,0)
x = int (input ("Enter the number of x:"))

i = 0
while (i < len(tup)):
    if (tup[i]==x):
        print("Number is found at index:",i)
        break
    else:
       print ("Number is not found")
    i+=1

#Print the elements of the following list using for loop. [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for el in list:
    print(el)
    

#Search for a number x in this tuple using for loop
tup = (1,6,4,5,3,2,0)
x = int (input ("Enter the number of x:"))

i = 0
for el in tup:
    if (x == el):
        print ("number is found at index:",i)
        break
    else:
        print("number not found")
    i+=1

#Print numbers from 1 to 100 using for loop
for el in range (1,101):
    print (el) 

#print numbers from 100 to 1
for el in range (100,0,-1):
    print(el)
  


    
 
