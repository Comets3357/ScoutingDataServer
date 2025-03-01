from extensions import db
from utils import getActiveEventKey
from .superscoutrecord import SuperScoutRecord
from .pitscoutrecord import PitScoutRecord
from .matchdata import MatchData
from .match_schedule import MatchSchedule
from .match_averages import MatchAverages

class TeamRecord(db.Model):
    __tablename__ = 'teams'
    teamNumber = db.Column(db.String(50), primary_key = True)
    teamName = db.Column(db.String(255))
    def __init__(self, teamNumber, teamName):
        self.teamNumber = teamNumber
        self.teamName = teamName
    
    def hasPitScoutData(self):
        return PitScoutRecord.query.filter_by(eventKey=getActiveEventKey(), teamNumber=self.teamNumber).count() > 0
    def hasSuperScoutData(self):
        return SuperScoutRecord.query.filter_by(eventKey=getActiveEventKey(), teamNumber=self.teamNumber).count() > 0
    def getMatchesPlayed(self):
        return MatchData.query.filter_by(eventKey=getActiveEventKey(), teamNumber=self.teamNumber).count()
    def getSuperScoutMatchesPlayed(self):
        return SuperScoutRecord.query.filter_by(eventKey=getActiveEventKey(), teamNumber=self.teamNumber).count()
    def getMatchesToPlay(self):
        count = 0
        count += MatchSchedule.query.filter_by(eventKey=getActiveEventKey(), matchLevel='qm', red1=self.teamNumber).count()
        count += MatchSchedule.query.filter_by(eventKey=getActiveEventKey(), matchLevel='qm', red2=self.teamNumber).count()
        count += MatchSchedule.query.filter_by(eventKey=getActiveEventKey(), matchLevel='qm', red3=self.teamNumber).count()
        count += MatchSchedule.query.filter_by(eventKey=getActiveEventKey(), matchLevel='qm', blue1=self.teamNumber).count()
        count += MatchSchedule.query.filter_by(eventKey=getActiveEventKey(), matchLevel='qm', blue2=self.teamNumber).count()
        count += MatchSchedule.query.filter_by(eventKey=getActiveEventKey(), matchLevel='qm', blue3=self.teamNumber).count()
        return count
    def allMatchesScouted(self):
        if self.getMatchesToPlay() == 0:
            return False
        else:
            return self.getMatchesPlayed() == self.getMatchesToPlay()
    def allMatchesSuperScouted(self):
        if self.getMatchesToPlay() == 0:
            return False
        else:
            return self.getSuperScoutMatchesPlayed() == self.getMatchesToPlay()
    def getPitScoutData(self):
        if (self.hasPitScoutData()):
            return PitScoutRecord.query.filter_by(eventKey=getActiveEventKey(), teamNumber=self.teamNumber).first()
        else:
            return None
        
    def getAverages(self):
        averages: MatchAverages = MatchAverages(self.teamNumber)
        if MatchData.query.filter_by(eventKey=getActiveEventKey(), teamNumber=self.teamNumber).count() > 0:
            for match in MatchData.query.filter_by(eventKey=getActiveEventKey(), teamNumber=self.teamNumber).all():
                averages.addAverage(match)
            averages.endgameShallow*=100
            #averages.climb = str(averages.climb)+"%"
            averages.endgameDeep*=100
            #averages.auto_leave = str(averages.auto_leave)+"%"
            return averages
        else:
            return None
    def getAverages(self):
        averages = MatchAverages(self.teamNumber)
        if MatchData.query.filter_by(eventKey=getActiveEventKey(), teamNumber=self.teamNumber).count() > 0:
            for match in MatchData.query.filter_by(eventKey=getActiveEventKey(), teamNumber=self.teamNumber).all():
                averages.addAverage(match)
            return averages
        else:
            return None
