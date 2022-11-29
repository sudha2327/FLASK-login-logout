from flask import *

app=Flask(__name__)
app.secret_key='sudha'

@app.route('/')

def home():
    return render_template('home.html')

@app.route('/login')

def login():
    return render_template('login.html')

@app.route('/success',methods=['POST'])

def success():
    if request.method=='POST':
        session['ename']=request.form['username']
        return render_template('success.html')

@app.route('/logout')

def logout():

    if 'ename' in session:
        session.pop('ename',None)

        return render_template('logout.html')
    else:

        return '<p>user alredy logged out</p>'

@app.route('/profile')

def profile():
    if 'ename' in session:
        email=session['ename']
        return render_template('profile.html',n=email)
    else:
        return '<p> please login first</p>'

if __name__=="__main__":
    app.run(debug=True)