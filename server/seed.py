from app import app, db
from model import Restaurant, Pizza, RestaurantPizza

def seed_data():
    with app.app_context():
        # Create Restaurants
        restaurant1 = Restaurant(name='Pizza Palace', address='123 Main St')
        restaurant2 = Restaurant(name='Italian Delight', address='456 Elm St')

        # Add Restaurants to session
        db.session.add_all([restaurant1, restaurant2])
        db.session.commit()

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
