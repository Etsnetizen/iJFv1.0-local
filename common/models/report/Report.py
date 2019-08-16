# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from application import db,app

class Report(db.Model):
    __tablename__ = 'report'

    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, nullable=False)
    attribute = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    name = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue())
    student_id = db.Column(db.BigInteger, server_default=db.FetchedValue())
    class_name = db.Column(db.String(500), server_default=db.FetchedValue())
    mobile = db.Column(db.String(11), nullable=False, server_default=db.FetchedValue())
    main_image = db.Column(db.String(100), server_default=db.FetchedValue())
    address = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue())
    description = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue())
    unable_deal_reason = db.Column(db.String(1000), server_default=db.FetchedValue())
    remark = db.Column(db.String(1000), server_default=db.FetchedValue())
    random_code = db.Column(db.String(255), server_default=db.FetchedValue())
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())

    @property
    def status_desc(self):
        return app.config['STATUS_MAPPING'][str(self.status)]

    @property
    def attribute_desc(self):
        return app.config['ATTRIBUTE_MAPPING'][str(self.attribute)]