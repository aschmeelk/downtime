from app import db
from datetime import date


class Calls(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_dn = db.Column(db.Date)
    franchise = db.Column(db.String(64))
    location = db.Column(db.String(64))
    machine = db.Column(db.String(64))
    status = db.Column(db.String(128))
    date_up = db.Column(db.Date)
    tech = db.Column(db.String(64))
    
    def __repr__(self):
        return '<Calls %r>' % (self.machine)


