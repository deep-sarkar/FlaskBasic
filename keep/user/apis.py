import json
from flask_restful import Resource
from flask import request

from .models import Users
from .validators import validate_registration_data


class Register_API(Resource):
    def post(self):
        req_data = request.data
        body = json.loads(req_data)

        try:
            ret = validate_registration_data(body)
            if 'error' in ret:
                return ret
            user = Users(**ret['data'])
            user.save()
        except Exception as e:
            return {'error': str(e), 'code': 500}

        return {'msg': 'success', 'code': 201}