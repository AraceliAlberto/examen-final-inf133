from app.database import db
class Reservations(db.Model):
    __tablename__ = "reservation"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer(), unique=True, nullable=False)
    restaurant_id = db.Column(db.Integer(), unique=True, nullable=False)
    reservation_date = db.Column(db.Date, nullable=False)
    num_guests = db.Column(db.Integer(), unique=True, nullable=False)
    special_requests = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)

    def __init__(self, user_id, restaurant_id, reservation_date, num_guests, special_requests, status):
        self.user_id = user_id
        self.restaurant_id = restaurant_id
        self.reservation_date = reservation_date
        self.num_guests = num_guests
        self.special_requests = special_requests
        self.status = status

    def save(self):
        db.session.add(self)
        db.session.commit()

@staticmethod
def get_all():
    return Reservations.query.all()
    
@staticmethod
def get_by_id(id):
    return db.session.get(Reservations, id)