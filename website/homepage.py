"""Routes to the websites landing page"""
from flask import Blueprint, render_template

homepage = Blueprint('homepage', __name__)

@homepage.route('/', methods=['GET', 'POST'])
def index():
    """Index page for the website"""
    return render_template('index.html')
