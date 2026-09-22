marks = {
    "Math": {"internal": 50, "external": 10},
    "Economics": {"internal": 30, "external": 30},
    "Biology": {"internal": 40, "external": 0},
    "English": {"internal": 20, "external": 20}
}

total_marks = 0

for subject, marks_data in marks.items():

    total = marks_data["internal"] + marks_data["external"]

    print(subject, ":", total)

    total_marks = total_marks + total

print("Total Marks:", total_marks)
