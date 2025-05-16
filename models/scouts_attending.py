from extensions import db

class ScoutsAttending(db.Model):
    __tablename__='scouts_attending'
    eventKey = db.Column(db.String(15), primary_key=True)
    scoutId = db.Column(db.Integer(), primary_key=True)
    thursday = db.Column(db.Integer())
    friday = db.Column(db.Integer())
    saturday = db.Column(db.Integer())
    sunday = db.Column(db.Integer())
