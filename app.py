from flask import Flask, render_template,url_for,request,redirect
import scoreCal


#Database Functions
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="",                              #Enter your MYSql Server Username and Password
  password="",
  database="answerbot"
)

mycursor = mydb.cursor()


app = Flask(__name__)


#Main Route to Home Page. 
#Shows Index Page with All the Saved Questions From Database and Set Initial Score to 0
@app.route('/')
def index():
	sql = "SELECT ques FROM master"
	mycursor.execute(sql)
	questions = mycursor.fetchall()
	score = 0
	return render_template('index.html', questions=questions, score=score)

#Route to Add Question to Database Page
@app.route('/add')
def add():
	return render_template('add.html')

#API Call to add the entered question to database
#Get the Values from form and commit it to database
@app.route('/addans', methods=['POST','GET'])
def addans():
	id = request.form['number']
	answer = request.form['answer']

	sql_command = "INSERT INTO master (id, ans) VALUES(%s,%s)"
	values = (id,answer)

	mycursor.execute(sql_command, values)

	mydb.commit()

	return redirect(url_for("index"))

#Method to Evaluate the Score.
#Gets the user selected question
#And Gets the user entered answer
#Call the function similarity_score() from scoreCal.py
#Give the score back to the index file
@app.route('/score',methods=['POST','GET'])
def score():
	id = request.form['questionNum']
	ans = id
	sql = "SELECT ans FROM master WHERE id = %s"

	values = (ans, )

	result = mycursor.execute(sql, values)
	result = mycursor.fetchall()
	result = result[0][0]  #The fetch all will return list of list (2D Matrix)

	answer = request.form['answer']
    #Calling the function from main.py
	score = round(scoreCal.similarity_score(result, answer), 2)
    
    #To Dislay the questions again
	sql = "SELECT ques FROM master"
	mycursor.execute(sql)
	questions = mycursor.fetchall()
	return render_template('index.html', questions=questions, score=score)



if __name__ == '__main__':
   app.run(debug = True, threaded=True)