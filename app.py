from flask import Flask
from routes.math_routes import math_blueprint
from database import db
import config
from cache_config import cache
from prometheus_flask_exporter import PrometheusMetrics  # type: ignore
from flask_jwt_extended import JWTManager

#Creeare aplicatia Flask
app = Flask(__name__)

#Configurare JWT
app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)

#Config app
app.config.from_object(config.Config)

#Cache local
app.config['CACHE_TYPE'] = 'SimpleCache'
app.config['CACHE_DEFAULT_TIMEOUT'] = 300
cache.init_app(app)

#Monitoring
metrics = PrometheusMetrics(app)

#DB
db.init_app(app)
app.register_blueprint(math_blueprint)

#Rulare aplicatie
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
