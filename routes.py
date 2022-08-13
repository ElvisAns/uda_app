from flask import Blueprint


urls = Blueprint(__name__)


@urls.route('/')
def index():
    pass

@urls.route('/animals')
def index():
    pass

@urls.route('/animal')
def index():
    pass

@urls.route('/animals/create')
def index():
    pass