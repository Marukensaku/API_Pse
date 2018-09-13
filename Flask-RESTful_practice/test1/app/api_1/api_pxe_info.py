import time

from app import db
from ..api_1 import api_1
from flask_restful import Api, Resource
from flask import jsonify, request
from app.models.pxeinfo import PxeInfo
from app.api_1.api_auth import auth

api_pxe_info = Api(api_1)


class TestApi(Resource):
    def get(self):
        return jsonify({'test_api': 'api is ok'})


class PxeInfoApi(Resource):
    # 添加信息
    @auth.login_required
    def post(self):
        pxe_info = request.get_json()
        print(pxe_info)
        print(type(pxe_info))
        try:
            pxe = PxeInfo(sn=pxe_info['sn'], pxe_ip=pxe_info['pxe_ip'], ilo_ip=pxe_info['ilo_ip'],
                          mac1=pxe_info['mac1'], mac2=pxe_info['mac2'], sw_name1=pxe_info['sw_name1'],
                          sw_name2=['sw_name2'], sw_port1=pxe_info['sw_port1'], sw_port2=pxe_info['sw_port2'])
            db.session.add(pxe)
            db.session.commit()
        except:
            print("{} PxeInfo add: {} failure...".format(time.strftime("%Y-%m-%d %H:%M:%S"), pxe_info['sn']))
            db.session.rollback()
            return False
        else:
            print("{} PxeInfo add: {} success...".format(time.strftime("%Y-%m-%d %H:%M:%S"), pxe_info['sn']))
            return True
        finally:
            db.session.close()

    # 根据GET方式传过来的sn值，查询结果
    @auth.login_required
    def get(self):
        s = request.args.get('sn')
        try:
            pxe_info = PxeInfo.query.filter_by(sn=s).order_by(PxeInfo.id.desc()).first()
            if pxe_info is None:
                print("{} PxeInfo query: {} failure...".format(time.strftime("%Y-%m-%d %H:%M:%S"), pxe_info['sn']))
                return False
            return pxe_info.to_json()
        except:
            print("{} PxeInfo query: {} failure...".format(time.strftime("%Y-%m-%d %H:%M:%S"), pxe_info['sn']))
            return False
        finally:
            db.session.close()


api_pxe_info.add_resource(TestApi, '/test_api', endpoint='test_api')
api_pxe_info.add_resource(PxeInfoApi, '/pxeinfo', endpoint='pxeinfo')