from flask import Flask
from .extensions import db
from .routes import register_routes
 
def create_app():
    print("=======1.Inside create_app function=====")
    app=Flask(__name__)

    #Configuration of databse
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///my_app_db.db'
    #optional:Disable modification tracking for performance
    app.config['SQLALCHEMY_TRACK_MODIFICATION']=False
    #Initialise extensions for the databse
    db.init_app(app)
    register_routes(app)

    with app.app_context():
        #create databse tables
        db.create_all()
 
    return app