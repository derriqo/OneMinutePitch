from flask import render_template,request, redirect,url_for,abort
from . import main
from .forms import UpdateProfile, PitchForm
from ..import db,photos
from flask_login import login_required, current_user
from ..models import User,Pitch


@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    

    return render_template('index.html')

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

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
    
@main.route('/pitch/new', methods = ['GET','POST'])
@login_required
def new_pitch():
    pitch_form = PitchForm()
    if pitch_form.validate_on_submit():
        title = pitch_form.title.data
        pitch = pitch_form.text.data
        category = pitch_form.category.data

        # Updated pitch instance
        new_pitch = Pitch(pitch_title=title,pitch_content=pitch,category=category,user=current_user,likes=0,dislikes=0)

        # Save pitch method
        new_pitch.save_pitch()
        return redirect(url_for('.index'))

    title = 'New pitch'
    return render_template('pitch.html',title = title,pitch_form=pitch_form )

@main.route('/pitches/startup_pitches')
def startup_pitches():

    pitches = Pitch.get_pitches('interview')

    return render_template("startup_pitches.html", pitches = pitches)

@main.route('/pitches/flirt_pitches')
def flirt_pitches():

    pitches = Pitch.get_pitches('flirt')

    return render_template("flirt_pitches.html", pitches = pitches)

@main.route('/pitches/inteligent_pitches')
def inteligent_pitches():

    pitches = Pitch.get_pitches('inteligent')

    return render_template("inteligent_pitches.html", pitches = pitches)


def user_pitches(uname):
    user = User.query.filter_by(username=uname).first()
    pitches = Pitch.query.filter_by(user_id = user.id).all()
    pitches_count = Pitch.count_pitches(uname)
    user_joined = user.date_joined.strftime('%b %d, %Y')
    return render_template("profile/pitches.html", user=user,pitches=pitches,pitches_count=pitches_count,date = user_joined)
