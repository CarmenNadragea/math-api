from flask import Flask
from routes.math_routes import math_blueprint
from database import db
import config

# Creează instanța aplicației Flask
app = Flask(__name__)

# Încarcă configurația aplicației (setări din config.py)
app.config.from_object(config.Config)

# Inițializează conexiunea la baza de date cu aplicația Flask
db.init_app(app)

# Înregistrează rutele API din blueprint-ul definit în math_routes.py
app.register_blueprint(math_blueprint)

# Când rulăm direct acest fișier: pornește aplicația
if __name__ == "__main__":
    # Asigură-te că baza de date e creată înainte de pornire
    with app.app_context():
        db.create_all()
    # Rulează serverul Flask în modul de depanare
    app.run(debug=True)
