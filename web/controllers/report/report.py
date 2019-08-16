from common.libs.UrlManager import UrlManager
from flask import Blueprint,request,redirect,jsonify,g
from common.libs.Helper import ops_render,getCurrentDate
from common.models.report.Report import Report
from sqlalchemy import or_#查询功能引入
from application import app,db
from common.models.User import User
from common.libs.Helper import iPagination
from common.libs.report.ReportService import ReportService
from common.models.log.OperationalRecordsLog import OperationalRecordsLog
route_index = Blueprint('index_page',__name__)
@route_index.route('/')
def index():
    resp_data = {}
    req = request.values


    page = int(req['p']) if ('p' in req and req['p']) else 1
    query = Report.query

    if 'mix_kw' in req:
        rule = or_( Report.name.ilike( "{0}".format( req['mix_kw']))
                    ,Report.mobile.ilike( "{0}".format(req['mix_kw'])))
        query = query.filter( rule )
    if 'status' in req and int(req['status']) in [1,0,-9,-8,-7]:
        query = query.filter(Report.status == req['status'])




    page_params = {
        'total':query.count(),
        'page_size':app.config['PAGE_SIZE'],
        'page':page,
        'display':app.config['PAGE_DISPLAY'],
        'url':request.full_path.replace("&p={}".format(page),"")
    }
    pages = iPagination( page_params )
    offset = (page - 1) * app.config['PAGE_SIZE']
    limit = app.config['PAGE_SIZE'] * page
    list = query.order_by( Report.id.desc() ).all()[offset:limit]
    resp_data['list'] = list
    resp_data['pages'] = pages
    resp_data['search_con'] = req
    resp_data['status_mapping'] = app.config['STATUS_MAPPING']
    return ops_render("report/index.html",resp_data )




@route_index.route('/ops',methods = ['POST'])
def report_ops():
    resp = {'code':200,'msg':"操作成功",'data':{} }
    req = request.values
    id = int(req['id']) if 'id' in req else 0
    act = req['act'] if 'act' in req else 0
    uid = int(req['uid']) if 'uid' in req else 0


    if not id :
        resp['code'] = -1
        resp['msg'] = '青选择要操作的报账单'
        return jsonify( resp )
    if not uid :
        resp['code'] = -1
        resp['msg'] = '非法登陆用户'
        return jsonify( resp )
    if act not in ['finish','unfinished','delay','processing','recover']:
        resp['code'] = -1
        resp['msg'] = '非法窜改操作'
        return jsonify( resp )
    user_info = User.query.filter_by(uid = uid).first()
    if not user_info:
        resp['code'] = -1
        resp['msg'] = '非法用户'
        return jsonify( resp )
    report_info = Report.query.filter_by(id = id).first()
    if not report_info:
        resp['code'] = -1
        resp['msg'] = '找不到报障单'
        return jsonify( resp )
    if act == 'finish':
        report_info.status = 1
    elif act == 'unfinished':
        report_info.status = 0
    elif act == 'delay':
        report_info.status = -9
    elif act == 'processing':
        report_info.status = -7
    elif act == 'recover':
        report_info.status = -8
    report_info.updated_time = getCurrentDate()
    db.session.add( report_info )
    db.session.commit()
    ReportService.setInfoChangeLog(id,app.config['STATUS_MAPPING'][str(report_info.status)],uid,'')
    return jsonify( resp )



@route_index.route('/info')
def info():
    resp_data = {}
    req = request.values

    id = int(req.get('id',0))
    reback_url = UrlManager.buildUrl('/')
    if id < 1:
        return redirect( reback_url )
    info = Report.query.filter_by( id = id ).first()
    if not info:
        return redirect( reback_url )


    resp_data['info'] = info
    page = int(req['p']) if ('p' in req and req['p']) else 1
    query = OperationalRecordsLog.query
    page_params = {
        'total':query.filter_by(report_id = id ).count(),
        'page_size':app.config['PAGE_SIZE'],
        'page':page,
        'display':app.config['PAGE_DISPLAY'],
        'url':request.full_path.replace("&p={}".format(page),"")
    }
    pages = iPagination( page_params )
    offset = (page - 1) * app.config['PAGE_SIZE']
    limit = app.config['PAGE_SIZE'] * page
    list = query.filter_by(report_id = id ).all()[offset:limit]
   # list = query.filter_by( uid = info.uid ).all()[offset:limit]


    resp_data['id'] = id
    resp_data['pages'] = pages
    resp_data['list'] = list
    return ops_render('/report/info.html',resp_data)


@route_index.route('/set',methods = ['POST','GET'])
def set():
    if request.method == 'GET':
        resp_data = {}
        req = request.args
        id = int(req.get('id',0))
        info = None
        if id :
            info = Report.query.filter_by(id=id).first()
            resp_data['info'] = info
            return ops_render('/report/set.html',resp_data)


    """
    POST
    """
    resp = {'code':200,'msg':'操作成功','data':{} }
    req = request.values

    id = int(req['id']) if 'id' in req else 0#报账单id
    uid = int(req['uid']) if 'uid' in req else 0#队员uid
    remark = req['remark'] if 'remark' in req else ''
    report_info = Report.query.filter_by(id = id).first()
    if report_info:
        model_report = report_info
        model_report.remark = remark
        model_report.updated_time = getCurrentDate()
        db.session.add( model_report )
        db.session.commit()
        ReportService.setInfoChangeLog(id,'改变备注',uid,remark)
        return jsonify( resp )
    else:
        resp['code'] = -1
        resp['msg'] = '查询不到此报账单'
        return jsonify( resp )

