from flask import Blueprint, render_template, request
from ..controllers.controllers import get_book_info, search_book

blueprint = Blueprint('main', __name__)

@blueprint.route('/', methods=['GET', 'POST'])
def return_index():
    if request.method == "POST":
        get_book_info()

    return render_template('index.html')

