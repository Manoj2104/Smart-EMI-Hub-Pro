from app.core.extensions import db

class LoanOffer(db.Model):
    __tablename__ = "loan_offers"

    id = db.Column(db.Integer, primary_key=True)
    bank_id = db.Column(db.Integer, db.ForeignKey("banks.id"), nullable=False)

    interest_rate = db.Column(db.Float, nullable=False)
    max_amount = db.Column(db.Integer)
    tenure_months = db.Column(db.Integer)

    approval_time = db.Column(db.String(100))
    affiliate_link = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<LoanOffer {self.bank_id} - {self.interest_rate}%>"