from init import db, ma
from sqlalchemy import Integer, String, DateTime, Column
import datetime, json

class LogDetails(db.Model):
    id = Column(Integer, primary_key = True)
    body = Column(String(1000), nullable = True)
    args = Column(String(1000), nullable = True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow )
    def __init__(self, body, args):
        self.body = json.dumps(body)
        self.args = json.dumps(args)
    def __repr__(self):
        return f"Id : {self.id}, Body : {self.body}, args = {self.args}, created_at = {self.created_at}"

#Schema
class LogSchema(ma.Schema):
    class Meta:
        fields=("id", "body", "args", "created_at")

log_schema = LogSchema()
logs_schema = LogSchema(many=True)