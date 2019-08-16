# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from application import db



class Image(db.Model):
    __tablename__ = 'image'

    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, nullable=False)
    file_key = db.Column(db.String(60), nullable=False, server_default=db.FetchedValue())
    random_code = db.Column(db.String(255), nullable=False)
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
