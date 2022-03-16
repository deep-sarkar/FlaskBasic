from .models import Users
from mongoengine.queryset.visitor import Q


def validate_registration_data(body):
    first_name = body.get('first_name')
    username = body.get('username')
    email_id = body.get('email_id')
    password = body.get('password')
    conf_password = body.get('conf_password')

    if not first_name:
        return {'error': 'first_name required.', 'code': 300}

    if password != conf_password:
        return {'error': "password didn't matched", 'code': 300}
    del body['conf_password']
    user = Users.objects.filter(Q(username=username) | Q(email_id=email_id))
    print(user)

    if user:
        return {'error': 'user already exists with this username or email', 'code': 300}

    return {'data': body}
