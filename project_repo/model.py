from init_db import db, ma
from datetime import datetime


class Project(db.Model):
    __tablename__ = "t_project"
    id = db.Column(db.Integer, primary_key=True)
    mon_dong = db.Column(db.String(10))
    logo = db.Column(db.String(50))
    name = db.Column(db.String(30))
    note = db.Column(db.String(100))
    platform = db.Column(db.String(10))
    status = db.Column(db.Integer)
    publish = db.Column(db.Integer)
    ins_dt = db.Column(db.String(10))
    fin_dt = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    def __init__(self, _id, mon_dong, name, note, platform, status, publish,
                 ins_dt, fin_dt):
        self.id = _id
        self.mon_dong = mon_dong
        self.name = name
        self.note = note
        self.platform = platform
        self.status = status
        self.publish = publish

    class ProjectSchema(ma.Schema):
        class Meta:
            fields = ("id", "name", "note")

    schema = ProjectSchema()
    schemas = ProjectSchema(many=True)
