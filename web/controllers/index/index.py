from flask import Blueprint,request,jsonify
route_index = Blueprint("index_page",__name__)
from common.libs.Helper import ops_render,getCurrentDate,Search,Check_If_Exceed_Maxsize
from common.models.report.Report import Report
from application import db,app
import time

@route_index.route('/',methods=['POST','GET'])
def index():
    if request.method == 'GET':
        return ops_render("/index/index.html")

    req = request.values

    ret = Search(req)
    resp_data = {}
    resp_data['search_info'] = None
    if ret:
        resp_data['search_info'] = ret['search_info']
        return ops_render('/index/search_result.html', resp_data)
    return ops_render('/index/search_result.html', resp_data)

@route_index.route('/about',methods = ['POST','GET'])
def about():
    if request.method == 'GET':
        return ops_render("/index/about.html")

    req = request.values
    ret = Search(req)
    resp_data = {}
    resp_data['search_info'] = None
    if ret :
        resp_data['search_info'] =  ret['search_info']
        return ops_render('/index/search_result.html',resp_data)
    return ops_render('/index/search_result.html',resp_data)


@route_index.route('/help',methods=['POST','GET'])
def help():
    if request.method == 'GET':
        return ops_render("/index/help.html")
    req = request.values
    ret = Search(req)
    resp_data = {}
    resp_data['search_info'] = None
    if ret:
        resp_data['search_info'] = ret['search_info']
        return ops_render('/index/search_result.html', resp_data)
    return ops_render('/index/search_result.html', resp_data)
@route_index.route('/report',methods=['POST','GET'])
def report():
    if request.method == 'GET':
        ret = Check_If_Exceed_Maxsize()
        report_check = {}
        report_check['notice'] = None
        if ret:
            return ops_render("/index/report.html", report_check)
        else:
            report_check['notice'] = '今天的生活区报障已报满，请明天再来，教师报障不受影响'
            return ops_render("/index/report.html", report_check)


    resp = {'code': 200, 'msg': '提交成功', 'data': {}}
    req = request.values
    mobile = req['search_mobile'] if 'search_mobile' in req else 0
     # 如果是搜索
    resp_data = {}
    if mobile == '':
        resp_data['search_info'] = None
        return ops_render('/index/search_result.html', resp_data)
    elif mobile == '-1':
        resp_data['search_info'] = None
        return ops_render('/index/search_result.html', resp_data)
    elif (mobile and mobile != ''):
        query = Report.query
        report_info = query.filter_by(mobile=mobile).order_by(Report.created_time.desc()).first()
        resp_data['search_info'] = report_info
        return ops_render('/index/search_result.html', resp_data)
    try:
        attribute = req['attribute'] if 'attribute' in req else -1
        #app.logger.info(attribute)
        #app.logger.info(type(attribute))
        if attribute == '-1' or attribute not in ['1','0']:
            resp['code'] = -1
            resp['msg'] = '操作有误'
            return jsonify( resp )

        name = req['name'] if 'name' in req else ''
        student_id = req['student_id'] if 'student_id' in req else 0
        class_name = req['class_name'] if 'class_name' in req else ''
        mobile = req['mobile'] if 'mobile' in req else ''
        address = req['address'] if 'address' in req else ''
        description = req['description'] if 'description' in req else ''

        #有效性
        #app.logger.info(getCurrentDate())#2019-09-29 18:18:16
        #app.logger.info(type(getCurrentDate()))#str
        ret = Check_If_Exceed_Maxsize()
        if (ret and attribute == '0') or (attribute == '1'):
            #如果没有超出限制并且是学生报障或者教师报障
            model_report = Report()
            model_report.member_id = 0
            model_report.name = name
            model_report.mobile = mobile
            model_report.address = address
            model_report.description = description
            model_report.attribute = attribute
            model_report.created_time = getCurrentDate()
            model_report.updated_time = getCurrentDate()
            if attribute == '0':#如果是学生报障
                model_report.student_id = student_id
                model_report.class_name = class_name
                db.session.add(model_report)
                db.session.commit()
                return jsonify( resp )
            elif attribute == '1':
                db.session.add( model_report )
                db.session.commit()
                return jsonify( resp )
        else:
            resp['code'] = -1
            resp['msg'] = '今日报障数量也超过最大限制，请明天再来'
            return jsonify( resp )
    except Exception as error:
        resp['code'] = -1
        resp['msg'] = '发生了不可预知错误，请联系管理员解决' + str(error)
        return jsonify( resp )


@route_index.route('/jfshop',methods = ['POST','GET'])
def shop():
    if request.method == 'GET':
        return ops_render("/index/shoppage.html")

    req = request.values
    ret = Search(req)
    resp_data = {}
    resp_data['search_info'] = None
    if ret :
        resp_data['search_info'] =  ret['search_info']
        return ops_render('/index/search_result.html',resp_data)
    return ops_render('/index/search_result.html',resp_data)

@route_index.route('/report/finish')
def finish():
    return ops_render('/index/finish.html')



