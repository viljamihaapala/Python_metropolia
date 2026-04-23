people = {
    "John": ["John", 30, "Engineer"],
    "Emily": ["Emily", 25, "Artist"],
    "Anna": ["Anna", 22, "Student"]
}

john_name = people["John"][0]
john_age = people["John"][1]
print("Johnin nimi:", john_name)
print("Johnin ikä:", john_age)

emily_job = people["Emily"][2]
print("Emilyn ammatti:", emily_job)

people["Anna"][2] = "Teacher"
people["James"] = ["James", 28, "Writer"]
people["Sophia"] = ["Sophia", 35, "Doctor"]

del people["Emily"]

print("\nLopullinen sanakirja:")
for key, value in people.items():
    print(key, ":", value)
