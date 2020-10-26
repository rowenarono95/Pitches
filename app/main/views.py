from flask import render_template
from . import main
from .forms import LoginForm,RegistrationForm
from flask_login import login_required,current_user



@main.route('/')
def index():
    return render_template ('index.html')


@main.route('/profile')
def profile():
    pass

