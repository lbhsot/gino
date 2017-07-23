from gino import Gino
from sqlalchemy import Column, BigInteger, Unicode

db = Gino()


class User(db.Model):
    __tablename__ = 'users'

    id = Column(BigInteger(), primary_key=True)
    nickname = Column(Unicode(), default='noname')

    def __repr__(self):
        return '{}<{}>'.format(self.nickname, self.id)
