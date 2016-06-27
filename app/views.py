from flask import render_template, flash, redirect
from app import app
from .forms import InputField, LoginForm

@app.route('/')
@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for name="%s", email="%s", remember_me=%s' %
              (form.name.data, form.email.data, str(form.remember_me.data)))
        return redirect('/intro')
    return render_template('login.html',title="Login",form=form)

@app.route('/intro')
def intro():
    return render_template('intro.html', title='Introduction', header='Introduction')

@app.route('/winterfell', methods=['GET','POST'])
def winterfell():
    form = InputField()
    return render_template('winterfell.html', title='Winterfell', header='Winterfell', form=form)

@app.route('/the_wall')
def the_wall():
    return render_template('the_wall.html', title='The Wall', header='The Wall')

@app.route('/northern_brothel')
def northern_brothel():
    return render_template('northern_brothel.html', title='Northern Brothel')
