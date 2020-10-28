from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import PitchesForm,UpdateProfile,CommentForm
from flask_login import login_required,current_user
from ..models import Pitches, User,Comment
from ..import db, photos



@main.route('/')
def index():
    
    # Getting reviews by category
    allPitches = Pitches.query.all()
    interview_piches = Pitches.get_pitches('interview')
    product_piches = Pitches.get_pitches('product')
    advertisement_pitches = Pitches.get_pitches('advertisement')


    return render_template('index.html', interview = interview_piches, product = product_piches, advertisement = advertisement_pitches,pitches = allPitches)

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

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/category/interview', methods=['POST','GET'])
def display_interview():
    pitches = Pitches.get_pitches('interview')
    return render_template('interview.html',interviewPitches=pitches)

@main.route('/category/advertisement', methods=['POST','GET'])
def display_advertisement():
    pitches = Pitches.get_pitches('advertisement')
    return render_template('advertisement.html',advertisementPitches=pitches)

@main.route('/category/product', methods=['POST','GET'])
def display_product():
    pitches = Pitches.get_pitches('product')
    return render_template('product.html',productPitches=pitches)      


@main.route('/pitch/<int:id>', methods=['GET', 'POST'])
@login_required
def comments(id):
    comments = Comment.get_comments(id)
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        comment = comment_form.text.data

        new_comment = Comment(comment = comment,user = current_user,pitch_id = id)

        new_comment.save_comment()


    return render_template("comments.html", comment_form = comment_form, comments = comments)      