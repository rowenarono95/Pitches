from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import PitchesForm
from flask_login import login_required,current_user
from ..models import Pitches, User



@main.route('/')
def index():
    return render_template ('index.html')


@main.route('/profile')
def profile():
    pass

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


