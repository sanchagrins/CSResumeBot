from mongoengine import *

class Resume(Document):
    author = StringField(required=True, max_length=50)
    url = URLField(required=True)
    post_date = StringField(required=True, max_length=25)
