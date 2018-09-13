

from flask import Blueprint

api_1 = Blueprint('api_1', __name__, url_prefix='/api')

from . import api_pxe_info, api_user, errors, api_auth