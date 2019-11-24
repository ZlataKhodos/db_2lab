import os

username = 'postgres'
password = 'postgres'
host = 'localhost'
port = '5432'
database = 'db2lab'
DATABASE_URI = os.getenv("DATABASE_URL",
                         'postgres://adohqioukvvabi:498ca1304f19777a437060222f5dba84b81381b916151c266c69720a9f5a64d4@ec2-54-75-230-253.eu-west-1.compute.amazonaws.com:5432/d9od5ls3jhj0g1')