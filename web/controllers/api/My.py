"""

报账单展示页面
"""
from web.controllers.api import route_api
from flask import request,g,jsonify
from common.models.report.Report import Report
from common.libs.UrlManager import UrlManager


@route_api.route('/my/report',methods = ['POST','GET'])
def myReportList():
    resp = {'code': 200, 'msg': '操作成功', 'data': {}}
    req = request.values

    member_info = g.member_info
    status = int(req['status']) if 'status' in req else 0
    query = Report.query.filter_by(member_id = g.member_info.id)
    if status == -7:
        query = query.filter(Report.status == -7)
    if status == -8:
        query = query.filter(Report.status == -8)
    elif status == -9:
        query = query.filter(Report.status == -9)
    elif status == 1:
        query = query.filter(Report.status == 1)
    elif status == 0:
        query = query.filter(Report.status == 0)
    elif status == 10:
        query = query.filter(Report.name != -1)


    pay_list = query.order_by(Report.id.desc())






    data_report_list = []
    if pay_list:
        for item in pay_list:
            tmp_data = {
                'status':item.status_desc,
                'created_time':item.created_time.strftime('%Y-%m-%d %H:%M:%S'),
                'unable_deal_reason':item.unable_deal_reason,
                'address':item.address,
                'pic_url':UrlManager.buildImageUrl(item.main_image)
            }
            data_report_list.append( tmp_data )

    resp['data']['report_list'] = data_report_list
    return jsonify( resp )



