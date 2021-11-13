import requests
import json
import mysql.connector

connection = mysql.connector.connect(host='localhost',database="lotnisko", user='root', password='')
mycursor = connection.cursor()

mycursor.execute("select * from samoloty")
samoloty = []
for samolot in mycursor:
    samoloty.append(samolot)

print(samoloty[0])