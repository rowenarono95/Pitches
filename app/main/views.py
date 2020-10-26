from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import PitchesForm,UpdateProfile
from flask_login import login_required,current_user
from ..models import Pitches, User
from ..import db



@main.route('/')
def index():
    return render_template ('index.html')


@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/pitch/new_pitches',methods=['POST','GET'])
@login_required
def new_pitch():
    pitch_form = PitchesForm()
    if pitch_form.validate_on_submit():
        pitch = pitch_form.text.data
        category = pitch_form.category.data


     # Updated pitch instance
        new_pitch = Pitches(pitch_comment=pitch,pitch_category=category,user=current_user)

        # Save pitch method
        new_pitch.save_pitch()
        return redirect(url_for('.index'))

    title = 'New pitch'
    return render_template('new_pitch.html',pitchform=pitch_form )



@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)