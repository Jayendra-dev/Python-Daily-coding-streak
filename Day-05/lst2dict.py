# Problem :keys=["name","age","city"]
#          Values=["Rahul",22,"Delhi"] se dictiponary banao
# Logic:zip()se dono ko add kro,phir dict()bana do.
# Solution:
keys = ["name", "age", "city"]
values = ["Rahul", 22, "Delhi"]

student = dict(zip(keys, values))
print(student) # Output: {'name': 'Rahul', 'age': 22, 'city': 'Delhi'}
