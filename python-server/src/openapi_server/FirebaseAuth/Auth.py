import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate(r"C:\Users\USER\PycharmProjects\Task Manager API with Authentication\python-server\src\openapi_server\FirebaseAuth\timesheet-ab3b6-firebase-adminsdk-fbsvc-d65e6b8a01.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://timesheet-ab3b6-default-rtdb.firebaseio.com/'
})
