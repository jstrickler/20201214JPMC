import requests

TEACHER_URL = "http://localhost:5000/api/teacher"  # <1>
STUDENT_URL = "http://localhost:5000/api/students/"

response = requests.get(TEACHER_URL)   # <2>
if response.status_code == requests.codes.OK:  # <3>
    print(response.content.decode())  # <4>
print('=' * 60)

for i in range(10):
    url = f"{STUDENT_URL}{i}"  # <5>
    response = requests.get(url)
    if response.status_code == requests.codes.OK:
        print(response.content.decode())
    print('-' * 60)
