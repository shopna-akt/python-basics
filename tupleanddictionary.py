#Tuple
tup = (3,1,2,5,0,1,3,4)
print (tup)
print (tup[2])
print (tup.count(1))

tup=()
print (tup)
print (type(tup))

tup = (1,)
print (tup)
print (type(tup))

tup = ("hello",)
print(tup)
print(type(tup))

#Dictionary
info = {
    "name" : "Shopna",
    "age":23,
    "department":"CSE",
    "marks":[66,85,45,97],
    "language":("C","Python","C","Javascript")
}
print (info)
print (info["name"])
print (info["age"])
print(info["marks"])
info["name"]="Sneha"
info["surname"]="Akter"
print(info)

null_dict = {}
null_dict["name"]= "Royes"
null_dict["age"]=16
null_dict["interests"]=("Programming","Racing","Gaming")
print(null_dict)

student={
    "name": "Liza",
    "id": 231,
    "score":{
        "physics":91,
        "chemistry":88,
        "math":95,
        "Geography":81

    }
}
print (student)
print (student["name"])
print(student["score"])
print(student["score"] ["math"])
print (student.keys())
print(student.values())
print(list(student.keys()))
print(list(student.values()))
print (student.items())
print(student.get("score"))
print(student.get("score1"))
new_info = {"cgpa":9.6,"dept":"CSE"}
student.update(new_info)
print(student)