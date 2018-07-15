import time
from firebase import firebase as fb
    
class Functions():
    def __init__(self):
        secret = ""
        url = ""
        username = ""

        auth = fb.FirebaseAuthentication(secret, username, True, True)

        self.fb = fb.FirebaseApplication(url, auth)

    def addMessage(self, name, email, message):
        timestamp = int(time.time())
        path = '/Messages/{0}'.format(timestamp)

        data = { 'name': name, 'email': email, 'message': message }

        try:
            p = self.fb.post(path, data)
            print(p)
            return True
        except:
            return False