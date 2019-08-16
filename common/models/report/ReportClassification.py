# coding: utf-8
from sqlalchemy import Column, Integer, String
from sqlalchemy.schema import FetchedValue
from application import db


class ReportClassification(db.Model):
    __tablename__ = 'report_classification'

    id = db.Column(db.Integer, primary_key=True)
    attribute = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue())
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
