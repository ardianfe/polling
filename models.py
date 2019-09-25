from app import db
from sqlalchemy.dialects.postgresql import JSON

class Result(db.Model):
    __tablename__ = 'result'

    id = db.Column(db.Integer, primary_key=True)
    hasil_lengkap = db.Column(db.JSON)
    
    def __init__(self, hasil_lengkap):
        self.hasil_lengkap = hasil_lengkap


