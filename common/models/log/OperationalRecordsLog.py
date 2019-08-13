# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from application import db



class OperationalRecordsLog(db.Model):
    __tablename__ = 'operational_records_log'

    id = db.Column(db.Integer, primary_key=True)
    report_id = db.Column(db.Integer, nullable=False)
    uid = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue())
    operation = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue())
    change_remark = db.Column(db.String(255))
    ua = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue())
    ip = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
