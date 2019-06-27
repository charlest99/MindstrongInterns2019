from flask import Flask, render_template, request
import os
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import datetime;

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "chats.db"))

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.secret_key = 'lmao'

db = SQLAlchemy(app)

i = 1
questions = ['test','How many people are in your immediate family?', 'Who are they?', 'How would you describe youre relationship with your family?', 
'Tell me about your favorite family members.','How did you meet your closest friends?','What do you like to do with your friends?',
'What is your favorite thing about your everyday life? Why?','What are your plans for the rest of the day?','What musicins do you enjoy listening to?',
'What songs would be on your playlist for the end of the world?','Did you play sports in school (high school/collage)? If yes, describe that experience.',
'What is your favorite tv show? What about it hold your interest?','What is your favorite movie? Why that movie?']
username = 'test'

class MyUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=False, primary_key=False)
    chats = db.Column(db.String(80), unique=False, nullable=False, primary_key=False)
    question = db.Column(db.String(80), unique=False, nullable=False, primary_key=False)
    time = db.Column(db.String(80), unique=False, nullable=False, primary_key=False)
    #add an integer for i to pass in
    #add the conversation
    def __repr__(self):
        return "<User: {}>".format(self.title)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/check',methods=['POST'])
def check():
	global username
	global i
	i = 1
	user_input=request.form['user_input']
	bot_response = "Send \"hello\" to begin!"
	username = user_input
	return render_template('index1.html',user_input=user_input,
		bot_response=bot_response
		)

@app.route('/process',methods=['POST'])
def process():
	global i
	global questions
	global username
	user_input=request.form['user_input']
	if (i < len(questions)):
		bot_response=questions[i]
		i = i+1
	else:
		bot_response = "done"
		i = 2
	print("Friend: "+bot_response)
	user1 = MyUser(title=username, chats = user_input, question=questions[i-2], time = datetime.datetime.now().timestamp())
	db.session.add(user1)
	db.session.commit()
	return render_template('index1.html',user_input=user_input,
		bot_response=bot_response
		)

@app.route('/hicontrast', methods=['GET', 'POST'])
def hicontrast():
    return render_template('hicontrast.html')


@app.route('/gonogo', methods=['GET', 'POST'])
def gonogo():
    return render_template('gonogo.html')

if __name__=='__main__':
	app.run(host='0.0.0.0', debug=True,port=5000)
