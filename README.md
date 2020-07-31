# Answer Checker Bot
A Simple Flask App to check user answers with the setter answers implemented using Soft Cosine Similarity.
## Overview
Users can enter question and respective answers and save it to database. Then users can select the question and give user answer and get a relevancy score ranging from 0 to 1 (Where 1 being the most accurate).
## Usage
Its requires MySQL Server for database operations. Download and install MySQL Server.
1. Git Clone the Repo
```python
git clone
```
2. Install the required packages. (pip3 for python 3.X.X >)
```python 
pip install -r requirements.txt 
```
3. Enter your MySQL server username and passowrd in create_database.py , create_table.py, and app.py scripts. <br>
4. Run the create_database.py then create_table.py to create the database and repesctive tables. <br>
5. Run the app.py
## Note
As gensim module take time to load, the flask server will load slowly and prediction will happen fast because flask application parameter threaded is set to TRUE.
