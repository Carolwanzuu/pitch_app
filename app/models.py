from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'

class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255))
    pitch_content = db.Column(db.String)
    category = db.Column(db.String(255))
    author = db.Column(db.String(255))
    upvote = db.Column(db.Integer)
    downvote = db.Column(db.Integer)        
    published_at = db.Column(db.DateTime, default = datetime.utcnow)    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment', backref = 'pitch', lazy = 'dynamic')