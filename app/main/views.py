from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User, Pitch, Category, Vote, Comment
from flask_login import login_required, current_user
from .forms import UpdateProfile,PitchForm,CategoryForm,CommentForm
from .. import db,photos

# views
@main.route('/')
def index():
    '''
    view root page function that returns the index page and its data
    '''

    category = Category.get_categories()

    return render_template('index.html',category = category)

@main.route('/add/category', methods=['GET','POST'])
@login_required
def new_category():
    '''
    view pitch page function that returns pitch categories page and its data
    '''
    form = CategoryForm()

    if form.validate_on_submit():
        name =form.name.data
        new_category = Category(name=name)
        new_category.save_category()

        return redirect(url_for('.index'))
    
    title = 'New category'
    return render_template('new_category.html', category_form = form,title=title)

    return render_template('pitch.html',pitch_id)    