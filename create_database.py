import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="",                #Write your MySql User Name
  password=""     #Write Your MySql Password
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE answerbot")