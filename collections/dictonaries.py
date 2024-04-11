#Dictoranies

# key = value pairs
# Key is the refrence, value is the data storage mechanism you want (int, string etc)


student1 = {
    "name": "susan",
    "stream": "tech",
    "completed_lessons": 4,
    "completed_lesson_names": ["variables", "data_types", "set_ups", "Collections"]

}

print(student1["name"])
print(student1["completed_lesson_names"][0])
student1["completed_lessons"] = 3
print(student1)
student1["completed_lesson_names"].remove("Collections")
print(student1["completed_lesson_names"])


# Getting the key for the dictionary
print(student1.keys())

