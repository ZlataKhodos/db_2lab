import os

username = 'postgres'
password = 'postgres'
host = 'localhost'
port = '5432'
database = 'db2lab'
DATABASE_URI = os.getenv("DATABASE_URL",
                         'postgres://ppopphllqvpued:99e48000ee0d0dbffb74073d91f187039a4b343fae154372238deb32ee108fe9@ec2-184-73-192-172.compute-1.amazonaws.com:5432/d4ic27tigd2so3')