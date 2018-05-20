from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

############################################################################
# 'message' table for storing direct messages transmitted through website. #
############################################################################
class Message(db.Model):
    __tablename__ = 'message'
    idMessage = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15))
    email = db.Column(db.String(30))
    message = db.Column(db.String(500))

    def __repr__(self):
        return '{0}'.format(self.idMessage)