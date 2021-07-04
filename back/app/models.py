from datetime import datetime

from mongoengine import Document, StringField, DateTimeField, ListField

from .settings import fernet


class Phrase(Document):
    title = StringField(unique=True, required=True, max_length=15)
    _secrets = ListField(required=False, null=True)
    created_at = DateTimeField(default=datetime.utcnow)

    def as_json(self, decoded=False):
        return {
            "id": str(self.pk),
            "title": self.title,
            "secrets": self.secrets if decoded else len(self.secrets),
            "created_at": self.created_at
        }

    @property
    def secrets(self):
        return [{
                "key": secret["key"],
                "message": fernet.decrypt(bytes(secret["message"], 'utf-8'))
            } for secret in self._secrets]

    def encrypt(self):
        for secret in self._secrets:
            message = secret["message"].encode()
            secret["message"] = fernet.encrypt(message).decode('utf-8')

    def set_secrets(self, raw_secrets):
        self._secrets = []
        for secret in raw_secrets:
            message = secret["message"].encode()
            secret["message"] = fernet.encrypt(message).decode('utf-8')
            self._secrets.append(secret)

    def __repr__(self):
        return f'<Phase {self.title}>'
