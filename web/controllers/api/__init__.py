from flask import Blueprint
route_api = Blueprint("api_page",__name__)
from web.controllers.api.Member import *
from web.controllers.api.report import *
from web.controllers.api.My import *
@route_api.route('/')
def index():
    return 'iGDPUJF Api Interface -1.0'