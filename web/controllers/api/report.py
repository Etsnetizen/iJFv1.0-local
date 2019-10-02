from web.controllers.api import route_api
from flask import request,jsonify,g
from common.models.report.ReportClassification import ReportClassification
from application import app,db
from common.models.Image import Image
from common.libs.UploadService import UploadService
from common.libs.UrlManager import UrlManager
from common.models.report.Report import Report
from common.libs.Helper import getCurrentDate,Check_If_Exceed_Maxsize
@route_api.route('/index/connect')
def connect():
    resp = {'code':200,'msg':'连接成功','data':{} }
    class_list = ReportClassification.query.filter_by(status = 1).all()
    if not class_list:
        resp['code'] = -1
        resp['msg'] = '获取不到分类信息'
        return jsonify( resp )
    data_class_list =  []
    for item in class_list:
         data_class_list.append( item.attribute )
    resp['data']['attribute'] = data_class_list
    return jsonify( resp )



@route_api.route('/submit',methods = ['POST'])
def SubmitReport():
    resp = {'code':200,'msg':'操作成功','data':{} }
    req = request.values

    attribute = req['attribute'] if 'attribute' in req else -1
    name = req['name'] if 'name' in req else ''
    student_id = req['student_id'] if 'student_id' in req else 0
    class_name = req['class_name'] if 'class_name' in req else ''
    mobile = req['mobile'] if 'mobile' in req else ''
    address = req['address'] if 'address' in req else ''
    description = req['description'] if 'description' in req else ''
    random_code = req['random_code'] if 'random_code' in req else 0


    if name is None or len(name) < 1:
        resp['code'] = -1
        resp['msg'] = '请输入符合规范的姓名'
        return jsonify(resp)
    if student_id is None or int(student_id)  < 10:
        resp['code'] = -1
        resp['msg'] = '请输入符合规范的学号'
        return jsonify(resp)
    if class_name is None or len(class_name) < 1:
        resp['code'] = -1
        resp['msg'] = '请输入符合规范的班级'
        return jsonify(resp)
    if mobile is None or len(mobile) < 11:
        resp['code'] = -1
        resp['msg'] = '请输入符合规范的手机'
        return jsonify(resp)
    if address is None or len( address ) < 1:
        resp['code'] = -1
        resp['msg'] = '请输入符合规范的地址'
        return jsonify(resp)
    if description is None or len( description ) < 1:
        resp['code'] = -1
        resp['msg'] = '请输入符合规范的描述'
        return jsonify(resp)


    image_info = Image.query.filter_by(random_code = random_code ).first()
    if image_info:
        #如果存在则说明他上传了图片
        model_report = Report.query.filter_by(random_code = random_code).first()
        model_report.attribute = attribute
        model_report.name = name
        model_report.student_id = student_id
        model_report.class_name = class_name
        model_report.mobile = mobile
        model_report.address = address
        model_report.description = description
        model_report.status = -8
        model_report.updated_time = getCurrentDate()
        db.session.add( model_report )
        db.session.commit()
    else :
        model_report = Report()
        model_report.name = name
        model_report.member_id = g.member_info.id
        model_report.attribute = attribute
        model_report.student_id = student_id
        model_report.class_name = class_name
        model_report.mobile = mobile
        model_report.address = address
        model_report.description = description
        model_report.status = -8
        model_report.updated_time = getCurrentDate()
        model_report.created_time = getCurrentDate()
        db.session.add(model_report)
        db.session.commit()



    return jsonify( resp )
@route_api.route('/submit/upload',methods = ['POST'])
def uploadImage():
    resp = {'code':200,'msg':'successfully!','data':{} }
    file_target = request.files
    app.logger.info(file_target)
    upfile = file_target['upfile'] if 'upfile' in file_target else None
    if upfile is None:
        resp['code'] = -1
        resp['msg'] = '上传失败'
        return jsonify( resp )
    ret = UploadService.uploadByFile( upfile )
    if ret['code'] != 200:
        resp['state'] = "上传失败" + ret['msg']
        return jsonify(resp)


    model_report = Report()
    model_report.member_id = g.member_info.id
    model_report.attribute = -1
    model_report.name = -1
    model_report.mobile = -1
    model_report.address = -1
    model_report.description = -1
    model_report.main_image = ret['data']['file_key']
    model_report.random_code = ret['data']['random_code']
    model_report.status = -1
    model_report.updated_time = getCurrentDate()
    model_report.created_time = getCurrentDate()
    db.session.add( model_report )
    db.session.commit()
    resp['data']['url'] = UrlManager.buildImageUrl(ret['data']['file_key'])
    resp['data']['random_code'] = ret['data']['random_code']
    return jsonify( resp )


@route_api.route('/index/check')
def check():
    resp = {'code':200,'msg':'连接成功','data':{} }
    ret = Check_If_Exceed_Maxsize()
    if ret == False:
        resp['code'] = -1
        resp['msg'] = '今日报障数量已满，请明天再来，教师报障不受影响'
        return jsonify( resp )






    return jsonify( resp )
