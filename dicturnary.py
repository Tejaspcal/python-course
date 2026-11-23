students = {
"dicturnay1" : {"name": "Conner", "class": "f-1", "subject": "science,math,english"},
"dicturnay2" : {"name": "John", "class": "f-2", "subject": "science,math,english"},
"dicturnay3" : {"name": "Smith", "class": "f-3", "subject": "science,math,english"},
"dicturnay4" : {"name": "David", "class": "f-4", "subject": "science,math,english"},
}

result = {}
seen_keys = []

for students_dicturnary, details in students.items():
    unique_key = (details['name'], details['class'])
    details_tuple = (details['subject'],)

    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[students_dicturnary] = {
            'name': details['name'],
            'class': details['class'],
            'subject': details_tuple
        }


for students_dicturnary, details in students.items():
    print(f"Student ID: {students_dicturnary}, Name: {details['name']}, Class: {details['class']}, Subjects: {details['subject']}")