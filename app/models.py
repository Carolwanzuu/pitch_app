from . import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    pitches = db.relationship('Pitch', backref = 'user', lazy = 'dynamic')

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

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key = True)    
    body = db.Column(db.String)          
    published_at = db.Column(db.DateTime, default = datetime.utcnow)    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))

    
    def save_comment(self):
        db.session.add(self)
        db.session.commit()