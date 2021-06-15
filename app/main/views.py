from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required
from ..models import User

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    return render_template('index.html')
@main.route('/user/<uname>')
def profile(uname):
    User = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    return render_template('profile.html',user = user)
