from .products import products_bp
from .employees import employees_bp
from .weather import weather_bp

 
def register_routes(app):
    print("=======2.Inside create_app function=====")
    app.register_blueprint(products_bp, url_prefix="/api/v1/products")
    app.register_blueprint(employees_bp, url_prefix="/api/v1/employees")
    app.register_blueprint(weather_bp, url_prefix="/api/v1/weather")
