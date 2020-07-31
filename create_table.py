import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="",                #Write your MySql User Name
  password="",     #Write Your MySql Password
  database="answerbot"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE master(id INT(10), ques TEXT, ans TEXT)")

