# sample
#connection with databse
from ..models.products import Product
from ..extensions import db

def fetch_products():
    print("******Inside product services:fetch_products function")
    products=Product.query.all()
    return [product.to_dict() for product in products]

def add_product(data):
    print("*******Inside product services : add_new_product function")
    #logic to create a new product
    #Logic to create a new product
    new_product=Product(
        name=data.get('name'),
        price=data.get('price'),
        sku=data.get('sku'),
        category=data.get('category'),
        in_stock=data.get('in_stock',True)
    )
    #Add to the database session and commit
    db.session.add(new_product)
    db.session.commit()
    return new_product.to_dict()
    #return {"id":3, "name":data.get("name")}

def get_product_by_id(product_id):
    print("*******Inside product services : get_product_by_id function")
    product=Product.query.get(product_id)
    if product:
        return product.to_dict()
    return None 

def update_product(product_id,data):
    print("**inside product services: update_product()****")
    product = Product.query.get(product_id)
    if not product:
        return None
    # None product details
    product.id = data.get('id', product.id)
    product.name = data.get('name', product.name)
    product.price = data.get('price', product.price)
    product.sku = data.get('sku' , product.sku)
    product.category = data.get('category' , product.category)
    product.in_stock = data.get('in_stock',product.in_stock)
    db.session.commit()
    return product.to_dict()
 
def delete_product(product_id):
    product=Product.query.get(product_id)
    if not product:
        return {"message":"product not found"},404
    db.session.delete(product)
    db.session.commit()
    return{"message":f"Product_id:{product_id} deleted successfully"},200