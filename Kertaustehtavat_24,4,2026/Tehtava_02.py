students = {
    "Matti": ["Matti", 5, "Matematiikka"],
    "Laura": ["Laura", 6, "Kuvataide"],
    "Oskari": ["Oskari", 4, "Liikunta"]
}

print(students["Matti"][1])
print(students["Laura"][2])

students["Oskari"][2] = "Historia"

students["Emma"] = ["Emma", 5, "Musiikki"]

del students["Laura"]

print(students)
