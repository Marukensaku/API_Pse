
from . import api_1
from flask import jsonify


@api_1.app_errorhandler(404)
def not_found(e):
    print(e)
    error_info = '{}'.format(e)
    response = jsonify({'error': error_info})
    response.status_code = 404
    return response


@api_1.app_errorhandler(403)
def forbidden(e):
    print(e)
    error_info = '{}'.format(e)
    response = jsonify({'error': error_info})
    response.status_code = 403
    return response