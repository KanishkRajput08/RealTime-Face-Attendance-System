import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':""
})

ref = db.reference('Students')

data = {
    "03513211921":
            {
                "name": "Vimal Barik",
                "major": "AI - DS",
                "starting_year": 2021,
                "total_attendance": 1,
                "standing": "B",
                "year": 4,
                "last_attendance_time": "2025-04-25 15:38:55"

            },
    "05113211921":
            {
                "name": "Vinayak Mishra",
                "major": "AI - DS",
                "starting_year": 2021,
                "total_attendance": 2,
                "standing": "B",
                "year": 4,
                "last_attendance_time": "2025-04-25 15:38:55"

            },
    "05213211921":
            {
                "name": "Prakash Mahatra",
                "major": "AI - DS",
                "starting_year": 2021,
                "total_attendance": 5,
                "standing": "G",
                "year": 4,
                "last_attendance_time": "2025-04-25 15:38:55"

            },
    "05313211921":
            {
                "name": "Kanishk",
                "major": "AI - DS",
                "starting_year": 2021,
                "total_attendance": 6,
                "standing": "G",
                "year": 4,
                "last_attendance_time": "2025-04-25 15:29:55"

            }

}

for key,value in data.items():
    ref.child(key).set(value)
