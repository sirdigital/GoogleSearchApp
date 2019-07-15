from main import db
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import text
import uuid


def generate_uuid():
    return str(uuid.uuid4())


class Result(db.Model):
    __tablename__ = 'search_results'

    id = db.Column(db.String(), primary_key=True, unique=True, default=generate_uuid)
    user_ip = db.Column(db.String())
    phrase = db.Column(db.String())
    links_and_positions = db.Column(JSON)
    total_results = db.Column(db.Integer)
    top_10_words = db.Column(JSON)
    created_at = db.Column(db.TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, user_ip, phrase, links_and_positions, total_results, top_10_words):
        self.user_ip = user_ip
        self.phrase = phrase
        self.links_and_positions = links_and_positions
        self.total_results = total_results
        self.top_10_words = top_10_words

    def __repr__(self):
        return '<id {}>'.format(self.id)
