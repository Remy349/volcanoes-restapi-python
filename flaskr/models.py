import sqlalchemy as sa
from flaskr.extensions import db


class Volcano(db.Model):
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String(100), index=True, unique=True)
    state = sa.Column(sa.String(20))
    height = sa.Column(sa.String(30))
    last_eruption = sa.Column(sa.String(30))

    def to_dict(self):
        data = {
            "id": self.id,
            "name": self.name,
            "state": self.state,
            "height": self.height,
            "last_eruption": self.last_eruption,
        }

        return data

    def __repr__(self):
        return f"""
            id: {self.id},
            name: {self.name}
        """


# from flaskr import db


# class Volcano(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(60), index=True, unique=True)
#     state = db.Column(db.String(20))
#     height = db.Column(db.String(30))
#     last_eruption = db.Column(db.String(30))

#     def to_dict(self):
#         data = {
#             "id": self.id,
#             "name": self.name,
#             "state": self.state,
#             "height": self.height,
#             "last_eruption": self.last_eruption
#         }

#         return data

#     def from_dict(self, data):
#         for field in data:
#             if field in data:
#                 setattr(self, field, data[field])
#
#     def __repr__(self):
#         return f"""
#             volcano:
#                 id: {self.id},
#                 name: {self.name},
#                 state: {self.state},
#                 height: {self.height},
#                 last_eruption: {self.last_eruption}
#         """
