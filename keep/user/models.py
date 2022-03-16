from mongoengine import Document, StringField, EmailField, BooleanField, DateTimeField
import datetime


class Users(Document):
    first_name = StringField(required=True)
    last_name = StringField()
    username = StringField(unique=True)
    password = StringField()
    email_id = EmailField(unique=True)
    is_active = BooleanField(default=False)
    dt_created = DateTimeField(default=datetime.datetime.now)
    dt_updated = DateTimeField(default=datetime.datetime.now)

    def __repr__(self):
        return 'user: {}'.format(self.username)

    def to_dict(self):
        user_dict = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'username': self.username,
            'email_id': self.email_id,
            'is_active': self.is_active,
            'dt_created': self.dt_created,
            'dt_updated': self.dt_updated
        }

        return user_dict
