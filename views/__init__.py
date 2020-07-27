from flask import Flask
from flask import Blueprint

app = Blueprint('views',__name__)


from . import account
from . import user
from . import order