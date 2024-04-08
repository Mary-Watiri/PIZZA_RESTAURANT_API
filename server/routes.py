from flask import jsonify, request, abort
from app import app, db
from model import Restaurant, Pizza, RestaurantPizza

# Route to get all restaurants
@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    try:
        restaurants = Restaurant.query.all()
        restaurant_list = [{'id': restaurant.id, 'name': restaurant.name, 'address': restaurant.address} for restaurant in restaurants]
        return jsonify(restaurant_list), 200
    except Exception as e:
        print(e)  # Print the error for debugging
        return jsonify({'message': 'Internal Server Error'}), 500

# Route to get a specific restaurant by ID
@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    try:
        restaurant = Restaurant.query.get(id)
        if restaurant is None:
            return jsonify({'message': 'Restaurant not found'}), 404
        restaurant_data = {
            'id': restaurant.id,
            'name': restaurant.name,
            'address': restaurant.address,
            'pizzas': [{'id': pizza.id, 'name': pizza.name, 'ingredients': pizza.ingredients} for pizza in restaurant.pizzas]
        }
        return jsonify(restaurant_data), 200
    except Exception as e:
        print(e)  # Print the error for debugging
        return jsonify({'message': 'Internal Server Error'}), 500

# Route to update a restaurant by ID
@app.route('/restaurants/<int:id>', methods=['PATCH'])
def update_restaurant(id):
    try:
        restaurant = Restaurant.query.get(id)
        if restaurant is None:
            return jsonify({'message': 'Restaurant not found'}), 404
        data = request.json
        if 'name' in data:
            restaurant.name = data['name']
        if 'address' in data:
            restaurant.address = data['address']
        db.session.commit()
        return jsonify({'message': 'Restaurant updated successfully'}), 200
    except Exception as e:
        print(e)  # Print the error for debugging
        return jsonify({'message': 'Internal Server Error'}), 500

# Route to create a new restaurant
@app.route('/restaurants', methods=['POST'])
def create_restaurant():
    try:
        data = request.json
        new_restaurant = Restaurant(name=data.get('name'), address=data.get('address'))
        db.session.add(new_restaurant)
        db.session.commit()
        return jsonify({'message': 'Restaurant created successfully'}), 201
    except Exception as e:
        print(e)  # Print the error for debugging
        return jsonify({'message': 'Internal Server Error'}), 500

# Route to delete a restaurant by ID
@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    try:
        restaurant = Restaurant.query.get(id)
        if restaurant is None:
            return jsonify({'message': 'Restaurant not found'}), 404
        db.session.delete(restaurant)
        db.session.commit()
        return jsonify({'message': 'Restaurant deleted successfully'}), 200
    except Exception as e:
        print(e)  # Print the error for debugging
        return jsonify({'message': 'Internal Server Error'}), 500
