collection = {1,2,3,"hello","World"}
print (collection)
print (type(collection))
print(len(collection))

collection = set()
print(type(collection))
collection.add(2)
collection.add(10)
collection.add(15)
collection.add(3)
collection.add("Shopna")
collection.add("Canada")
print (collection)
collection.remove(3)
print (collection)
collection.pop()
print(collection)
collection.clear()
print(collection)

set1 = {1,2,3}
set2 = {2,4,3}
print (set1.intersection(set2))
print (set2.union(set1))