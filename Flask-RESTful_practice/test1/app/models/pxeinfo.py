import datetime
from flask import jsonify
from app import db


class PxeInfo(db.Model):
    __tablename__ = 'PxeInfo'
    id = db.Column(db.Integer, primary_key=True)
    sn = db.Column(db.String(64), index=True)
    pxe_ip = db.Column(db.String(64))
    ilo_ip = db.Column(db.String(64))
    mac1 = db.Column(db.String(64))
    mac2 = db.Column(db.String(64))
    sw_name1 = db.Column(db.String(64))
    sw_name2 = db.Column(db.String(64))
    sw_port1 = db.Column(db.String(64))
    sw_port2 = db.Column(db.String(64))
    info_time = db.Column(db.DateTime)

    def __init__(self, sn, pxe_ip, ilo_ip, mac1, mac2, sw_name1, sw_name2, sw_port1, sw_port2):
        self.sn = sn
        self.pxe_ip = pxe_ip
        self.ilo_ip = ilo_ip
        self.mac1 = mac1
        self.mac2 = mac2
        self.sw_name1 = sw_name1
        self.sw_name2 = sw_name2
        self.sw_port1 = sw_port1
        self.sw_port2 = sw_port2
        self.info_time = datetime.datetime.now()

    def to_json(self):
        j = jsonify({'id': self.id, 'sn': self.sn, 'pxe_ip': self.pxe_ip, 'ilo_ip': self.ilo_ip, 'mac1': self.mac1,
                     'mac2': self.mac2, 'sw_name1': self.sw_name1, 'sw_name2': self.sw_name2, 'sw_port1': self.sw_port1,
                     'sw_port2': self.sw_port2, 'info_time': self.info_time})
        return j

    def __repr__(self):
        return "<PxeInfo {}>".format(self.sn)