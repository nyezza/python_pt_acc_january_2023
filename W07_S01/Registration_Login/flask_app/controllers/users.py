from flask_app import app
from flask_app.models.user import User
from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt(app)


# =================Index Page=====================
@app.route('/')
def index():
    return render_template("index.html")
# =========================REGISTER======================
@app.route('/users/create', methods = ['post'])
def register():
    if User.validate(request.form):
        hashed_password = bcrypt.generate_password_hash(request.form['password'])
        # 11111111 === $2b$12$QF5fd.Xw7p2CPewJP8e2F.lmBnK9VykCw4XZuUPHPnZf477q/n1wa
        # 22222222 === $2b$12$koIBD209RYV3buJMOWtvpefLBiWc82TjIhU6qS9CBhLtdhg.H3oGi
        # user_data ={
        #     'first_name': request.form['first_name'],
        #     'last_name': request.form['last_name'],
        #     'email': request.form['email'],
        #     'password': hashed_password
        # }
        user_data = {
            **request.form,
            'password':hashed_password
        }
        print(request.form['password'] ,"="*10, hashed_password)
        session['user_id'] = User.create_user(user_data)
        # print("-"*10, user_id, "-"*10)
        return redirect('/dashboard')
    print("Data is not valid")
    return render_template("index.html")

# ============================LOGIN=========================
@app.route('/users/login', methods=['post'])
def login():
    # Verify Email
    user_from_db = User.get_by_email({'email':request.form['email']})
    print("+"*10, user_from_db,'+'*10)
    if user_from_db:
        if not bcrypt.check_password_hash(user_from_db.password, request.form['password']):
            flash("Invalid Email/Password")
            return redirect('/')
        else:
            session['user_id'] = user_from_db.id
            return redirect('/dashboard')
    flash("Invalid Email/Password")
    return redirect('/')

@app.route('/dashboard')
def dashboard():
    user = User.get_by_id({'id':session['user_id']})
    return render_template("dashboard.html", user = user)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')