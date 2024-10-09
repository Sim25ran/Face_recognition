import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendancerealtime-56570-default-rtdb.firebaseio.com/"
})

ref=db.reference('Students')

data={
    "23654":
        {
            "name":"Neymar",
            "major":"Football",
            "starting_year":2017,
            "total_attendance":6,
            "standing":"G",
            "year":4,
            "last_attendance_time":"2024-10-01 00:54:34"
        }  ,
        "56498":
        {
            "name":"Virat Kohli",
            "major":"Cricket",
            "starting_year":2015,
            "total_attendance":4,
            "standing":"E",
            "year":6,
            "last_attendance_time":"2024-10-07 08:01:26"
        }  ,
          "67895":
        {
            "name":"Rohit Sharma",
            "major":"Cricket",
            "starting_year":2016,
            "total_attendance":9,
            "standing":"G",
            "year":3,
            "last_attendance_time":"2024-09-30 11:13:29"
        } ,
          "96251":
        {
            "name":"Simran Kukreja",
            "major":"Data Science",
            "starting_year":2021,
            "total_attendance":12,
            "standing":"G",
            "year":3,
            "last_attendance_time":"2024-10-07 08:11:26"
        } 
        
}

for key, value in data.items():
    ref.child(key).set(value)