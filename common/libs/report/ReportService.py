"""
记录对报账单的操作
"""
from application import db
from common.models.report.Report import Report
from common.libs.Helper import getCurrentDate
from common.models.log.OperationalRecordsLog import OperationalRecordsLog
from common.models.User import User
class ReportService():
    @staticmethod
    def setInfoChangeLog(report_id=0,operation = '',member_uid = 0,remark=''):
        if report_id < 1 or member_uid < 1 or not operation:
            return False
        report_info = Report.query.filter_by(id = report_id ).first()
        if not report_info:
            return False
        user_info = User.query.filter_by(uid=member_uid).first()
        model_info_change = OperationalRecordsLog()
        model_info_change.nickname = user_info.nickname
        model_info_change.uid = member_uid
        model_info_change.report_id = report_id
        model_info_change.operation = operation
        model_info_change.change_remark = remark
        model_info_change.created_time = getCurrentDate()
        db.session.add(model_info_change)
        db.session.commit()
        return True

