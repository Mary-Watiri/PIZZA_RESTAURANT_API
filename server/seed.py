from app import app, db
from model import Restaurant, Pizza, RestaurantPizza

def seed_data():
    with app.app_context():
        # Create Restaurants with unique names
        restaurant1 = Restaurant(name='Pizza Palace', address='123 Main St')
        restaurant2 = Restaurant(name='Italian Delight', address='456 Elm St')
        restaurant3 = Restaurant(name="My Unique Pizzeria", address="789 Maple St")

        # Add Restaurants to session
        db.session.add_all([restaurant1, restaurant2, restaurant3])
        db.session.commit()

        # Serialize Restaurants after committing to database
        serialized_restaurants = []
        for restaurant in Restaurant.query.all():  
            serialized_restaurants.append(restaurant.to_dict())

        print("Serialized Restaurants:")
        for restaurant_dict in serialized_restaurants:
            print(restaurant_dict)

        # Create Pizzas
        cheese_pizza = Pizza(name='Cheese', ingredients='Dough, Tomato Sauce, Cheese')
        pepperoni_pizza = Pizza(name='Pepperoni', ingredients='Dough, Tomato Sauce, Cheese, Pepperoni')

        # Add Pizzas to session
        db.session.add_all([cheese_pizza, pepperoni_pizza])
        db.session.commit()

        # Create RestaurantPizzas with prices
        restaurant_pizza1 = RestaurantPizza(restaurant_id=restaurant1.id, pizza_id=cheese_pizza.id, price=10.99)
        restaurant_pizza2 = RestaurantPizza(restaurant_id=restaurant2.id, pizza_id=pepperoni_pizza.id, price=12.99)

        # Add RestaurantPizzas to session
        db.session.add_all([restaurant_pizza1, restaurant_pizza2])
        db.session.commit()

if __name__ == '__main__':
    seed_data()
