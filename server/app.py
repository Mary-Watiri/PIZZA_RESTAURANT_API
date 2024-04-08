from flask import Flask
from model import db, Restaurant, Pizza, RestaurantPizza
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza_restaurants.db'

# Initialize SQLAlchemy instance
db.init_app(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Import routes after initializing Flask app and db to avoid circular import
import routes

if __name__ == '__main__':
    app.run(debug=True)