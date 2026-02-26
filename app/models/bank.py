from app.core.extensions import db

class Bank(db.Model):
    __tablename__ = "banks"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    logo = db.Column(db.String(255))  # image path
    rating = db.Column(db.Float, default=4.0)
    processing_fee = db.Column(db.String(100))

    offers = db.relationship("LoanOffer", backref="bank", lazy=True)

    def __repr__(self):
        return f"<Bank {self.name}>"