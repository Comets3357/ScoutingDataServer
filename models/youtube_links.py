from extensions import db

class YoutubeLinks(db.Model):
    __tablename__='youtube_links'
    eventKey = db.Column(db.String(15), primary_key=True)
    matchNumber = db.Column(db.Integer(), primary_key=True)
    youtubeKey = db.Column(db.String(15))