from web.interceptors.Authinterceptor import *
from web.interceptors.Errorinterceptors import *
from web.interceptors.ApiAuthinterceptor import *
from application import app

from web.controllers.user.user import route_user
from web.controllers.static import route_static
from web.controllers.report.report import route_index
from web.controllers.api import route_api



app.register_blueprint(route_user,url_prefix='/user')
app.register_blueprint(route_static,url_prefix='/static')
app.register_blueprint(route_index,url_prefix='/')
app.register_blueprint(route_api,url_prefix='/api')