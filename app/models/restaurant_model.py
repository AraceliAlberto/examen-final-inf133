from app.database import db

class Restaurant(db.Model):
    __tablename__ = "restaurant"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Float(), nullable=False)

    def __init__(self, name, address, city, phone, description, rating):
        self.name = name
        self.address = address
        self.city = city
        self.phone = phone
        self.description = description
        self.rating = rating

    def save(self):
        db.session.add(self)
        db.session.commit()

@staticmethod
def get_all():
    return Restaurant.query.all()
    
@staticmethod
def get_by_id(id):
    return db.session.get(Restaurant, id)