#database model for product

#importing db instance from extensions.py
from ..extensions import db

class Product(db.Model):
    __tablename__="products"

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    price=db.Column(db.Float,nullable=False)
    sku=db.Column(db.String(100))
    category=db.Column(db.String(100))
    in_stock=db.Column(db.Boolean,default=True)

    def to_dict(self):
        return {
            "id":self.id,
            "name":self.name,
            "price":self.price,
            "sku":self.sku,
            "category":self.category,
            "in_stock":self.in_stock
        }