from extensions import db

class Scouts(db.Model):
    __tablename__ = 'scouts'
    scoutId = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    scout_first_name = db.Column(db.String(255))
    scout_last_name = db.Column(db.String(255))
    scout_team = db.Column(db.String(10))