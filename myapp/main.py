import pyrebase

firebaseConfig = {
  'apiKey': "AIzaSyBKmMkOE0QuLgLBw2-Prq3gWvGcUz17N0A",
  'authDomain': "fir-authentication-aabe3.firebaseapp.com",
  'databaseURL': "https://fir-authentication-aabe3-default-rtdb.firebaseio.com",
  'projectId': "fir-authentication-aabe3",
  'storageBucket': "fir-authentication-aabe3.appspot.com",
  'messagingSenderId': "625103438647",
  'appId': "1:625103438647:web:0bce87f8f096e405d910b2",
}

firebase=pyrebase.initialize_app(firebaseConfig)
auth= firebase.auth()
database=firebase.database()


email = input("Enter your email: ")
passs = input("Enter your password: ")
user_auth=auth.create_user_with_email_and_password(email,passs)
print("Succesfull")