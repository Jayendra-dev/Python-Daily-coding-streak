# Concept :Dict me key na mile to error ki jagah default value dena.
# problem:student={"name":"Rahul","age":22} 
# Task :marks key nikalna h.Agar na mile to 0.
student = {"name": "Rahul", "age": 22}
marks = student.get("marks", 0)  # Key nahi hai to 0 dega
print(marks)  # Output: 0
