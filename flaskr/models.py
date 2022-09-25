from flaskr import db


class Volcano(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), index=True, unique=True)
    state = db.Column(db.String(20))
    height = db.Column(db.String(30))
    last_eruption = db.Column(db.String(30))
    
    def __repr__(self):
        return f"""
            volcano:
                id: {self.id},
                name: {self.name},
                state: {self.state},
                height: {self.height},
                last_eruption: {self.last_eruption}
        """

