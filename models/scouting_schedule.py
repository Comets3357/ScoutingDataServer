from extensions import db

class ScoutingSchedule(db.Model):
    __tablename__='scouting_schedule'
    eventKey = db.Column(db.String(15), primary_key=True)
    matchNumber = db.Column(db.Integer(), primary_key=True)
    teamNumber = db.Column(db.String(10), primary_key=True)
    scoutId = db.Column(db.Integer())
    