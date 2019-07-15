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

i = 0
questions = ['test','Please state your date of birth.','How many people are in your immediate family?','Who are they?','How would you describe your relationship with your family?','Tell me about your favorite family members.','Tell me about your extended family.','Do you have a best friend?','How did you meet your closest friends?','What do you like to do with your friends?',
'What is your favorite food? Why?','What’s your favorite animal? Why?','What is the cutest animal?','What is your favorite thing about your everyday life? Why?','Who provides you the most happiness? Why?','What activity gives you joy? Why?','How do you define joy','What productive things have you done this week?',
'Where did you grow up?','What made you decide to participate in this study?','Why are you living in this state?','What life advice would you give to the youth?','How was your week?','What is the one thing that could make you happy, but you refuse to do it because you’re afraid of what others would think?',
'What are your plans for the rest of the day?','What are your goals for accomplishment by the end of the year?','What do you want to do with your life?','What state do you live in?','Who is your hero?','What do you believe in?','It’s a lovely day isn’t it?',
'What’s your favorite genre of music?','Who is your favorite artist?','What artists do you enjoy listening to?','When did you first start listening to music on your own for entertainment?','What made you start?','What songs would be on your playlist for the end of the world?','Do you prefer to listen to music live?',
'Why or why not?','What do you use to listen to music and why?','Why do you listen to music?','What is/are your least favorite genre(s) of music? Why?','Do you have a least favorite music creator?','Who and why or why not','What is your favorite song lyric to quote?,Why?','What is/are your favorite sport(s) to play?',
'What about that sport do you like?','Did you play sports in school (high school/college)? If yes, describe that experience.','Have you experienced any injuries while playing? If yes, describe that experience.','Is there a sport you wish you had played? If yes, what sport and why?','What is/are your favorite sport(s) to watch?',
'What about that sport do you like?','Who do you watch sports with?','What do you like about watching sports?','Who is/are your favorite team(s)?','Who is your favorite player?','What about that player do you like?','Have you ever watched a team play in person? If yes, describe that experience.','Do you dislike playing or watching any sports? Why?',
'A is taller than R, but only with her high heels on; without them, she is taller than only N. I is shorter than C but taller than A with her high heels on. Y is taller than R, but shorter than I. Who is the tallest person in the room?','What is the product of three and five?',
'What is the quotient of 25 and five?','What are the possible answers to 1+1 = ?','What is a hundred and eighty three minus eighty three?','There are three boxes. One is labeled "APPLES" another is labeled "ORANGES". The last one is labeled "APPLES AND ORANGES". You know that each is labeled incorrectly. You may ask me to pick one fruit from one box which you choose. How can you label the boxes correctly?',
'Are music videos films? Why or why not?','Who is your favorite actor?','Do you have a favorite filmmaker?','Do you have a favorite franchise?','What is journalism?','What is your favorite genre of television? Of movies?','What is your favorite tv show? What about it holds your interest?','What is your favorite movie? Why that movie?','What separates paparazzi and sensationalism from true media?','What makes a good source?',
'What news sources do you find trustworthy, and why?','What technology is most important for newspapers and online news sources to take advantage of in telling their stories?','What makes information unimportant?']
usernamed = 'test'
username = ''
score = 0

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
	global questions
	questions = ['YOU ARE DONE!','Please state your date of birth.','How many people are in your immediate family?','Who are they?','How would you describe your relationship with your family?','Tell me about your favorite family members.','Tell me about your extended family.','Do you have a best friend?','How did you meet your closest friends?','What do you like to do with your friends?',
'What is your favorite food? Why?','What’s your favorite animal? Why?','What is the cutest animal?','What is your favorite thing about your everyday life? Why?','Who provides you the most happiness? Why?','What activity gives you joy? Why?','How do you define joy','What productive things have you done this week?',
'Where did you grow up?','What made you decide to participate in this study?','Why are you living in this state?','What life advice would you give to the youth?','How was your week?','What is the one thing that could make you happy, but you refuse to do it because you’re afraid of what others would think?',
'What are your plans for the rest of the day?','What are your goals for accomplishment by the end of the year?','What do you want to do with your life?','What state do you live in?','Who is your hero?','What do you believe in?','It’s a lovely day isn’t it?',
'What’s your favorite genre of music?','Who is your favorite artist?','What artists do you enjoy listening to?','When did you first start listening to music on your own for entertainment?','What made you start?','What songs would be on your playlist for the end of the world?','Do you prefer to listen to music live?',
'Why or why not?','What do you use to listen to music and why?','Why do you listen to music?','What is/are your least favorite genre(s) of music? Why?','Do you have a least favorite music creator?','Who and why or why not','What is your favorite song lyric to quote?,Why?','What is/are your favorite sport(s) to play?',
'What about that sport do you like?','Did you play sports in school (high school/college)? If yes, describe that experience.','Have you experienced any injuries while playing? If yes, describe that experience.','Is there a sport you wish you had played? If yes, what sport and why?','What is/are your favorite sport(s) to watch?',
'What about that sport do you like?','Who do you watch sports with?','What do you like about watching sports?','Who is/are your favorite team(s)?','Who is your favorite player?','What about that player do you like?','Have you ever watched a team play in person? If yes, describe that experience.','Do you dislike playing or watching any sports? Why?',
'Are music videos films? Why or why not?','Who is your favorite actor?','Do you have a favorite filmmaker?','Do you have a favorite franchise?','What is journalism?','What is your favorite genre of television? Of movies?','What is your favorite tv show? What about it holds your interest?','What is your favorite movie? Why that movie?','What separates paparazzi and sensationalism from true media?','What makes a good source?',
'What news sources do you find trustworthy, and why?','What technology is most important for newspapers and online news sources to take advantage of in telling their stories?','What makes information unimportant?']
	return render_template('index.html')

@app.route('/partOne',methods=['POST'])
def partOne():
	global username
	global i
	i = 0
	user_input=request.form['user_input']
	username = user_input
	return render_template('home.html', user=username)

@app.route('/home', methods=['GET', 'POST'])
def home():
	global username
	return render_template('home.html', user=username)



@app.route('/index1', methods=['GET','POST'])
def index1():
	return render_template('index1.html', user_input='', bot_response='Type Hello to begin!')

@app.route('/process',methods=['POST'])
def process():
	global questions
	global username
	global i
	global score
	user_input=request.form['user_input']
	if(score > 4000):
		bot_response = "done"
		print("DONE")
		print("DONE")
		print("DONE")
		print("DONE")
		i = 0
	elif (i < len(questions)):
		bot_response=questions[1]
		x = questions.pop(0)
		questions.append(x)
		i = i+1
	else:
		bot_response = "done"
		print("DONE")
		print("DONE")
		print("DONE")
		print("DONE")
		i = 0
	print("Friend: "+bot_response)
	score +=len(user_input)
	print(score)
	user1 = MyUser(title=username, chats = user_input, question=questions[0], time = datetime.datetime.now().timestamp())
	db.session.add(user1)
	db.session.commit()
	return render_template('index1.html',user_input=user_input,
		bot_response=bot_response
		)

@app.route('/hicontrastinstructions', methods=['GET', 'POST'])
def hicontrastinstructions():
	global username
	return render_template('hicontrastinstructions.html', user=username)


@app.route('/audioodballinstructions', methods=['GET', 'POST'])
def audioodballinstructions():
	global username
	return render_template('audioodballinstructions.html', user=username)

@app.route('/indexPageinstructions', methods=['GET', 'POST'])
def indexPageinstructions():
	global username
	return render_template('indexPageinstructions.html', user=username)

@app.route('/hicontrast', methods=['GET', 'POST'])
def hicontrast():
	global username
	return render_template('hicontrast.html', user=username)



@app.route('/audioodball', methods=['GET', 'POST'])
def audioodball():
	global username
	return render_template('audioodball.html', user=username)

@app.route('/helpme', methods=['GET', 'POST'])
def helpme():
	global username
	print("HELP PLEASE")
	print("HELP PLEASE")
	print("HELP PLEASE")
	print("HELP PLEASE")
	print("HELP PLEASE")
	print("HELP PLEASE")
	return render_template('helpme.html', user=username)

if __name__=='__main__':
	app.run(host='0.0.0.0', debug=True,port=5000)