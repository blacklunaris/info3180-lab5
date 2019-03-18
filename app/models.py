from . import db

class UserProfile(db.Model):
    id = db.Column(db.String(7), primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    username = db.Column(db.String(80))
    email = db.Column(db.String(80))
    gender = db.Column(db.String(10))
    bio = db.Column(db.String(255))
    created = db.Column(db.DateTime())
    pic = db.Column(db.String(80))
    


    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.userid)  # python 2 support
        except NameError:
            return str(self.userid)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)
        

        
