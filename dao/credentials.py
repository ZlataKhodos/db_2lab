import os

username = 'gbegxrbhllsuwm'
password = '977e87ef99ff23ee342aaa88b2f7ae18ae9ebaa29c8acfe859bad1b6895bc0af'
host = 'ec2-184-73-192-172.compute-1.amazonaws.com'
port = '5432'
database = 'd9rgqqe18dne49'
DATABASE_URI = os.getenv("DATABASE_URL",
                         'postgres://ppopphllqvpued:99e48000ee0d0dbffb74073d91f187039a4b343fae154372238deb32ee108fe9@ec2-184-73-192-172.compute-1.amazonaws.com:5432/d4ic27tigd2so3')