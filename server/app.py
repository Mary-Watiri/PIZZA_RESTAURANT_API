from flask import Flask, jsonify, request, make_response
from model import db, Restaurant, Pizza, RestaurantPizza
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza_restaurants.db'

# Initialize SQLAlchemy instance
db.init_app(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

@app.route('/')
def index():
    return '<h1>RESTAURANTS</h1>'

@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([{'id': r.id, 'name': r.name, 'address': r.address} for r in restaurants])

@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get_or_404(id)
    return jsonify({
        'id': restaurant.id,
        'name': restaurant.name,
        'address': restaurant.address,
        'pizzas': [{'id': p.id, 'name': p.name, 'ingredients': p.ingredients} for p in restaurant.pizzas]
    }), 200



@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.json
    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')


    if price is None or pizza_id is None or restaurant_id is None:
        return jsonify({'errors': ['Missing required fields']}), 400

    
    pizza = Pizza.query.get(pizza_id)
    restaurant = Restaurant.query.get(restaurant_id)
    if pizza is None or restaurant is None:
        return jsonify({'errors': ['Pizza or Restaurant not found']}), 404

    
    response_data = {
        'id': pizza.id,
        'name': pizza.name,
        'ingredients': pizza.ingredients
    }

    return jsonify(response_data), 201



@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    
    if restaurant is None:
        return jsonify({'error': 'Restaurant not found'}), 404
    
    RestaurantPizza.query.filter_by(restaurant_id=id).delete()

    db.session.delete(restaurant)
    db.session.commit()

    return jsonify({'message': 'Restaurant deleted successfully'}), 200

@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    
    pizza_list = []
    for pizza in pizzas:
        pizza_info = {
            'id': pizza.id,
            'name': pizza.name,
            'ingredients': pizza.ingredients
        }
        pizza_list.append(pizza_info)
    
    return jsonify(pizza_list), 200


if __name__ == '__main__':
    app.run(debug=True)
