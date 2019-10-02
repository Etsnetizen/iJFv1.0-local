from flask import render_template,g
import datetime
from common.models.report.Report import Report
import time
from application import app
def ops_render (template,context = {}):#context初始化为字典，不一定要传值
    if "current_user" in g:
        context['current_user'] = g.current_user
    return render_template(template,**context)

def getCurrentDate( format = "%Y-%m-%d %H:%M:%S"):
    app.logger.info(datetime.datetime.now().strftime( "%Y-%m-%d %H:%M:%S" ))
    return datetime.datetime.now().strftime( format )

def iPagination( params ):
    import math

    ret = {
        "is_prev":1,#是否有上一页
        "is_next":1,#是否有下一页
        "from" :0 ,#用于循环
        "end":0,
        "current":0,#当前页
        "total_pages":0,#总共有多少页
        "page_size" : 0,#
        "total" : 0,
        "url":params['url']
    }

    total = int( params['total'] )
    page_size = int( params['page_size'] )
    page = int( params['page'] )
    display = int( params['display'] )
    total_pages = int( math.ceil( total / page_size ) )
    total_pages = total_pages if total_pages > 0 else 1
    if page <= 1:
        ret['is_prev'] = 0

    if page >= total_pages:
        ret['is_next'] = 0

    semi = int( math.ceil( display / 2 ) )

    if page - semi > 0 :
        ret['from'] = page - semi
    else:
        ret['from'] = 1

    if page + semi <= total_pages :
        ret['end'] = page + semi
    else:
        ret['end'] = total_pages

    ret['current'] = page
    ret['total_pages'] = total_pages
    ret['page_size'] = page_size
    ret['total'] = total
    ret['range'] = range( ret['from'],ret['end'] + 1 )
    return ret

def Search(req):
    resp = {}
    mobile = req['search_mobile'] if 'search_mobile' in req else 0
    app.logger.info(mobile)
    if mobile == '' :
        return None
    if int(mobile) == -1:
        return None
    query = Report.query
    report_info = query.filter_by(mobile=mobile).order_by(Report.created_time.desc()).first()
    if not report_info:
        return None
    resp['search_info'] = report_info
    return resp


def Check_If_Exceed_Maxsize():
    #检查是否超出最大限制报障数量
    present_time = getCurrentDate()
    origin_day_time = getCurrentDate("%Y-%m-%d") + " 00:00:00"
    app.logger.info(present_time)
    app.logger.info(origin_day_time)
    report_today_count = Report.query.filter(origin_day_time < Report.created_time
                                             ,Report.created_time < present_time).filter_by(attribute = 0).count()

    app.logger.info(report_today_count)


    report_today_list = Report.query.filter(origin_day_time < Report.created_time
                                             ,Report.created_time < present_time).all()
    app.logger.info(report_today_list)


    if report_today_count + 1 > app.config['MAXSIZE_OF_REPORT'] :
        return False
    return True





