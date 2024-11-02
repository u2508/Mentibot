from flask import Flask,render_template, request, jsonify,flash,url_for,make_response
import random ,pandas as pd
from flask import render_template as render,request,jsonify,redirect,session
from werkzeug.security import generate_password_hash, check_password_hash
import secrets,datetime
secret_key = secrets.token_hex(16)  # Generates a 32-character hexadecimal string
api_key='0eda083fd1bffbbfa30e3946e54ed9a2'
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()

app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///mood.db"
app.config['SQLALCHEMY_DATABASE_URI1']="sqlite:///userbase.db"
app.secret_key=secret_key
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    date=db.Column(db.DateTime,default=datetime.datetime.now)
    def __repr__(self):
        return f'<User {self.name } - {self.email} - {self.password}>'
class MoodEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mood = db.Column(db.String(50))
    note = db.Column(db.String(200))
    date = db.Column(db.DateTime, default=datetime.datetime.now)

    # Database initialization
db.init_app(app)
with app.app_context():
    db.create_all()
@app.route('/')
def renderinit():
        return render("login.html")
    # Route for user registration
@app.route('/register', methods=['POST'])
def register():
        data = request.get_json()
        name = data['name']
        email = data['email']
        password = data['password']

    # Check if email already exists
        if User.query.filter_by(email=email).first():
            return jsonify({'success': False, 'message': 'User already exists!'})

    # Create a new user
        hashed_password = generate_password_hash(password)
        new_user = User(name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'success': True})

    # Route for user login
@app.route('/login', methods=['POST'])
def login():
        data = request.get_json()
        email = data['email']
        password = data['password']

    # Find the user in the database
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return jsonify({'success': True})
        else:
            return jsonify({'success': False, 'message': 'Incorrect email or password!'})
@app.route('/logout', methods=['POST'])
def logout():
    # Clear the user session or perform other logout operations
        session.clear()  # or session.pop('user', None) for more specific clearing
        flash('You have been logged out successfully!', 'success')
        return redirect(url_for('index'))  # Redirect to homepage or login page
@app.route('/index')
def index():
        if 'user_id' in session:
            return render("index.html")  # Replace with your weather page template or data
        else:
            return redirect('/')  # Redirect to login if not logged in
    # Mental Health Chatbot Route
@app.route('/chatbot')
def chatbot():
        return render_template('chatbot.html')

@app.route('/chatbot/respond', methods=['POST'])
def chatbot_response():
        user_message = request.form['message']
        # Dummy response logic for now
        responses = ["Stay positive!", "Take it one day at a time.", "Reach out if you need support."]
        bot_message = random.choice(responses)
        return jsonify({'message': bot_message})

    # Mood Tracker Route
@app.route('/mood-tracker-data', methods=['POST'])
def mood_tracker():

            mood = request.form['mood']
            note = request.form['note']
            mood_entry = MoodEntry(mood=mood, note=note)
            db.session.add(mood_entry)
            db.session.commit()
            return('',200)

@app.route('/mood-tracker')
def mood_render():
    return render_template('mood_tracker.html')
@app.route('/mood-tracker/data')
def get_mood_data():
        entries = MoodEntry.query.all()
        mood_data = [{'date': entry.date, 'mood': entry.mood , 'note': entry.note} for entry in entries]

        return jsonify(mood_data)

    # Stress Management Route
@app.route('/stress-management')
def stress_management():
        return render_template('stress_management.html')

@app.route('/export-data')
def export_data():
    mood_entries = MoodEntry.query.all()
    data = [{'Mood': entry.mood, 'Note': entry.note, 'Date': entry.date.strftime("%Y-%m-%d")} for entry in mood_entries]
    df = pd.DataFrame(data)
    csv = df.to_csv(index=False)
    response = make_response(csv)
    response.headers["Content-Disposition"] = "attachment; filename=mood_data.csv"
    response.headers["Content-type"] = "text/csv"
    return response

if __name__ == '__main__':
    app.run(debug=True)
