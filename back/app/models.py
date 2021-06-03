import base64
import hashlib
import hmac
from datetime import datetime

from mongoengine import Document, StringField, DateTimeField, ListField

from .settings import SECRET_KEY, fernet


class Phrase(Document):
    key = StringField(unique=True, required=True, max_length=200)
    _message = StringField(required=False, null=True, max_length=200)
    created_at = DateTimeField(default=datetime.utcnow)
    tags = ListField(StringField(max_length=50))

    @property
    def as_json(self):
        return {
            "id": str(self.pk),
            "key": self.key,
            "message": self.message,
            "created_at": self.created_at,
            "tags": self.tags
        }

    @property
    def message(self):
        return fernet.decrypt(bytes(self._message, 'utf-8'))

    def set_message(self, message):
        message = message.encode()
        self._message = fernet.encrypt(message).decode('utf-8')

    def __repr__(self):
        return f'<Phase {self.key}>'
