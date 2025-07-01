<<<<<<< HEAD
from flask import Blueprint, render_template, request
from ..controllers.controllers import get_book_info, search_book

blueprint = Blueprint('main', __name__)

@blueprint.route('/', methods=['GET', 'POST'])
def return_index():
    if request.method == "POST":
        get_book_info()

=======
from flask import Blueprint, render_template

blueprint = Blueprint('main', __name__)

@blueprint.route('/', methods=['GET'])
def return_index():
>>>>>>> 2d077b513ed70c4283e9295240fea592b83a36eb
    return render_template('index.html') 
