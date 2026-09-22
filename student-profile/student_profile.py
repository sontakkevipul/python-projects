batch = [
    "Python Foundation - Batch 1",
    "Python Foundation - Batch 2",
    "Git Beginner Batch 1"
]

course = ["Python", "Git", "Docker", "Linux"]

batch_dict = {
    course[0]: [
        {
            "Batch": batch[0],
            "start_batch": "March 2026",
            "Type": "weekday",
            "module": (
                "Variables",
                "operators",
                "data types",
                "OOPS",
                "functions"
            )
        },
        {
            "Batch": batch[1],
            "start_batch": "July 2026",
            "Type": "weekend",
            "module": (
                "Variables",
                "operators",
                "data types",
                "OOPS",
                "functions"
            )
        }
    ],

    course[1]: [
        {
            "Batch": batch[2],
            "start_batch": "May 2026",
            "Type": "weekday",
            "module": (
                "merge",
                "commit",
                "push",
                "pull",
                "branch"
            )
        }
    ]
}

student = {
    "name": "Shivam Namdev",
    "email": "shivamnamdev@gmail.com",
    "city": "Pune",
    "batch": batch[1],
    "student_id": 101
}

completed_skills = (
    "Variables",
    "Strings",
    "Lists",
    "Tuples"
)

enrolled_courses = []
total_skills = 0

for course_name, batches in batch_dict.items():

    for batch_info in batches:

        if batch_info["Batch"] == student["batch"]:

            enrolled_courses.append(course_name)
            total_skills += len(batch_info["module"])

completed_count = len(completed_skills)

progress = (completed_count / total_skills) * 100

print("\n========== STUDENT PROFILE ==========")

print(f"Name       : {student['name']}")
print(f"Email      : {student['email']}")
print(f"Batch      : {student['batch']}")
print(f"Location   : {student['city']}")

print("\nEnrolled Courses:")
for c in enrolled_courses:
    print(f"- {c}")

print("\nCompleted Skills:")
for skill in completed_skills:
    print(f"- {skill}")

print(f"\nTotal Skills       : {total_skills}")
print(f"Completed Skills   : {completed_count}")
print(f"Progress           : {progress:.2f}%")

print("\nAttendance: Regular")
print("Status             : In Progress")

print("======================================")
