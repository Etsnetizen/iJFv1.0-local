from flask import Blueprint
from flask import request,jsonify,make_response,redirect
from common.models.User import User
from common.libs.user.UserService import UserService
import json
from application import app,db
from common.libs.Helper import ops_render
from flask import g
from common.libs.UrlManager import UrlManager

route_user = Blueprint('user_page',__name__,template_folder='templates')

@route_user.route('/login',methods = ['GET','POST'])
def login():
    if request.method == 'GET':
        return ops_render('user/login.html')



    resp = {'code':200,'msg':'操作成功','data':{} }
    req = request.values
    login_name = req['login_name'] if 'login_name' in req else ''
    login_pwd = req['login_pwd'] if 'login_pwd' in req else ''

    if login_name is None or len(login_name) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入正确的用户名"
        return jsonify(resp)
    if login_pwd is None or len(login_pwd) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入正确的密码"
        return jsonify(resp)
    user_info = User.query.filter_by(login_name=login_name).first()
    if not user_info:
        resp['code'] = -1
        resp['msg'] = "请输入正确的账号与密码"
        return jsonify(resp)
    if user_info.status == 0:
        resp['code'] = -1
        resp['msg'] = "此账号已被禁止登陆"
        return jsonify(resp)

    if user_info.login_pwd != UserService.genePwd(login_pwd,user_info.login_salt):
        resp['code'] = -1
        resp['msg'] = "请输入正确的账号与密码"
        return jsonify(resp)

    response = make_response(json.dumps( resp ))
    response.set_cookie(app.config['AUTH_COOKIE_NAME'],"%s#%s"%(UserService.geneAuthCode( user_info ),user_info.uid))
    return response



@route_user.route('/logout')
def logout():
    response = make_response(redirect(UrlManager.buildUrl("/user/login")))
    response.delete_cookie(app.config['AUTH_COOKIE_NAME'])
    return response

