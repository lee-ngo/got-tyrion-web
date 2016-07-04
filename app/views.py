from flask import render_template, flash, redirect
from app import app
# from .forms import InputField, LoginForm

@app.route('/')
@app.route('/intro')
def intro():
    return render_template('intro.html', title='Introduction')

# @app.route('/login', methods=['GET','POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         flash('Login requested for name="%s", email="%s", remember_me=%s' %
#               (form.name.data, form.email.data, str(form.remember_me.data)))
#         return redirect('/intro')
#     return render_template('login.html',title="Login",form=form)

@app.route('/winterfell', methods=['GET','POST'])
def winterfell():
    # form = InputField()
    return render_template('winterfell.html', title='Winterfell')

@app.route('/the_wall')
def the_wall():
    return render_template('the_wall.html', title='The Wall')

@app.route('/brothel')
def brothel():
    return render_template('brothel.html', title='Northern Brothel')

@app.route('/tavern')
def tavern():
    return render_template('tavern.html', title='Northern Tavern')

@app.route('/death')
def death():
    return render_template('death.html', title='You have died.')

@app.route('/the_vale')
def the_vale():
    return render_template('the_vale.html', title='The Vale')

@app.route('/trial')
def trial():
    return render_template('trial.html',title="Trial by Combat")

@app.route('/kings_landing')
def kings_landing():
    return render_template('kings_landing.html',title="King's Landing")

@app.route('/small_council')
def small_council():
    return render_template('small_council.html',title="Small Council")
