# Write your Python code below:
# with open('myfile.txt', 'r') as file:
#     lines = file.readlines()
#     total_lines = len(lines)

# print(f"Total lines: {total_lines}")

# Print Student Profile
# Write your Python code below:

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
            "module": ("Variables", "operators", "data types", "OOPS", "functions")
        },
        {
            "Batch": batch[1],
            "start_batch": "July 2026",
            "Type": "weekend",
            "module": ("Variables", "operators", "data types", "OOPS", "functions")
        }
    ],

    course[1]: [
        {
            "Batch": batch[2],
            "start_batch": "May 2026",
            "Type": "weekday",
            "module": ("merge", "commit", "push", "pull", "branch")
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

# Completed skills
completed_skills = ("Variables", "Strings", "Lists", "Tuples")
print(" ")

# Find the course and batch details
enrolled_courses = []
total_skills = 0

for course_name, batches in batch_dict.items():

    for batch_info in batches:

        if batch_info["Batch"] == student["batch"]:

            enrolled_courses.append(course_name)

            total_skills += len(batch_info["module"])


# Calculate progress
completed_count = len(completed_skills)

progress = (completed_count / total_skills) * 100


# Print Student Profile
l = []

(l.append("\n========== STUDENT PROFILE =========="))

l.append(f"\nName       : {student['name']}")
l.append(f"\nEmail      : {student['email']}")
l.append(f"\nBatch      : {student['batch']}")
l.append(f"\nLocation   : {student['city']}")
l.append("\n ")

l.append("\nCreds: Username: user_name") 
l.append ("\nPassword: Password@123")
l.append("\n ")

l.append("\n\nEnrolled Courses:")
for c in enrolled_courses:
    l.append(f"\n- {c}")

l.append("\nCompleted Skills:")
for skill in completed_skills:
    l.append(f"\n- {skill}")

l.append(f"\nTotal Skills       : {total_skills}")
l.append(f"\nCompleted Skills   : {completed_count}")
l.append(f"\nProgress           : {progress:.2f}%")
l.append("\n ")

l.append("\nAttendance: Regular")
l.append("\nStatus             : In Progress")

l.append("\n======================================")


with open("myfile.txt","r") as file:
    print(file.read())
