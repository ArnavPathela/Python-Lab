from main import app 
from flask import render_template,request,session,url_for,redirect,flash
from flask import session
from applications.model import *
from sqlalchemy.exc import IntegrityError

@app.route('/') #checks if user is registered then renders dashboard otherwise tells to login or register
def home():
    if 'email' not in session: 
        return redirect(url_for('youlog'))
    return render_template('dash.html')

@app.route('/youlog')  #if user is not logged in
def youlog():
    return render_template('youlog.html')

@app.route('/login', methods=['GET', 'POST']) #login route
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        email = request.form.get('email', None)
        password = request.form.get('password', None)

        if not email:
            flash('Email is required')
            return redirect(url_for('login'))
        if not password:
            flash('Password is required')
            return redirect(url_for('login'))
        
        u = User.query.filter_by(email=email).first()  
        if not u:
            flash('Invalid email')
            return redirect(url_for('login'))
        
        if u.password == password:  
            session['email'] = email 
            flash('Logged in successfully')
            return redirect(url_for('home'))  
        else:
            flash('Invalid password')
            return redirect(url_for('login'))

@app.route('/logout') #logout route
def logout():
    session.pop('email', None) 
    print("session after logout", session)  
    return redirect(url_for('home'))  

@app.route('/register', methods=['GET', 'POST']) #register route
def register():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        email = request.form.get('email', None)
        password = request.form.get('password', None)

        if not email:
            flash('Email is required')
            return redirect(url_for('register'))
        if not password:
            flash('Password is required')
            return redirect(url_for('register'))
        
        new_user = User(email=email, password=password)

        try:
            db.session.add(new_user)
            db.session.commit()
            flash('User created successfully')
            return redirect(url_for('login'))
        
        except IntegrityError:
            db.session.rollback()  # Rollback the session to avoid transaction issues
            flash('Email already exists')
            return redirect(url_for('register'))
    
@app.route('/dash')  #dashboard route
def dash():
    return render_template('dash.html') 



@app.route('/add', methods=['GET', 'POST']) #route for add journal 
def add():
    if 'email' not in session:
        flash("Please log in first.")
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')

        # Validate form fields
        if not title:
            flash('Title is required')
        if not content:
            flash('Content is required')

        if not title or not content:
            flash('All fields are required')
            return redirect(url_for('add'))
        
        # Get the user from the session email
        user = User.query.filter_by(email=session['email']).first()
        
        # Create and save the journal entry with the user's ID
        addd = Journal(title=title, content=content, user_id=user.id)
        
        try:
            db.session.add(addd)
            db.session.commit()
            flash('Journal added successfully')
            return redirect(url_for('dash'))
        except Exception as e:
            db.session.rollback()
            flash(f'An error occurred: {str(e)}')
        
        return redirect(url_for('add'))
    
    return render_template('add.html')



@app.route('/view')  #view journal
def view():
    if 'email' not in session:
        flash("Please log in first.")
        return redirect(url_for('login'))
    
    user = User.query.filter_by(email=session['email']).first()
    if user is None:
        flash("User not found. Please log in again.")
        return redirect(url_for('login'))
    
    journals = Journal.query.filter_by(user_id=user.id).all()
    return render_template('view.html', journals=journals)





@app.route('/delete/<int:id>', methods=['POST']) #delete journal in app
def delete(id):
    if 'email' not in session:
        flash("Please log in first.")
        return redirect(url_for('login'))
    
    journal = Journal.query.get_or_404(id)
    
    # Check if the logged-in user is the owner of the journal
    if journal.user.email != session['email']:
        flash("You do not have permission to delete this journal.")
        return redirect(url_for('view'))

    try:
        db.session.delete(journal)
        db.session.commit()
        flash("Journal deleted successfully")
    except Exception as e:
        db.session.rollback()
        flash(f"An error occurred: {str(e)}")
    
    return redirect(url_for('view'))

@app.route('/edit/<int:id>', methods=['GET', 'POST']) #app route for edit 
def edit(id):
    if 'email' not in session:
        flash("Please log in first.")
        return redirect(url_for('login'))

    journal = Journal.query.get_or_404(id)

    # Check if the logged-in user is the owner of the journal
    if journal.user.email != session['email']:
        flash("You do not have permission to edit this journal.")
        return redirect(url_for('view'))

    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')

        # Validate input
        if not title or not content:
            flash("Both title and content are required.")
            return redirect(url_for('edit', id=id))

        try:
            journal.title = title
            journal.content = content
            db.session.commit()
            flash("Journal updated successfully.")
            return redirect(url_for('view'))
        except Exception as e:
            db.session.rollback()
            flash(f"An error occurred: {str(e)}")
            return redirect(url_for('edit', id=id))

    # Render the form with the existing data
    return render_template('edit.html', journal=journal)
