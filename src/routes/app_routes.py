from flask import Blueprint, render_template

blueprint = Blueprint('main', __name__)

@blueprint.route('/', methods=['GET'])
def return_index():
    return render_template('index.html') 
