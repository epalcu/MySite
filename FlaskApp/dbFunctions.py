import dbTables as dt
from flask_sqlalchemy import SQLAlchemy
    
class Functions():
    def __init__(self, database):
        self.db = database
        self.session = self.db.session

    def addMessage(self, name, email, message):
        m = dt.Message(name=name, email=email, message=message)
            
        self.session.add(m)
        self.session.commit()

        return True