# PIZZA_RESTAURANT_API
This project implements a Flask-based API for a pizza ordering system. It allows users to manage restaurants, pizzas, and their associations through various API endpoints.

## Features:
<ol>
<li>Restaurant Management:</li>
<p>Create, retrieve, and delete restaurants with basic validation (name length and uniqueness).</p>
<li>Pizza Management:</li>
<p>Retrieve all pizzas.</p>
<li>Restaurant-Pizza Association:</li>
<p>Create associations between existing restaurants and pizzas, specifying a price.</p>
<p>Validates that required fields (price, pizza_id, restaurant_id) are provided.</p>
</ol>

## Setup:
<ol>
<li>Install Dependencies:</li>
<p>pip install flask flask-sqlalchemy sqlalchemy</p>
<li>Database Configuration</li>
<p>SQLALCHEMY_DATABASE_URI = 'sqlite:///pizza_restaurant.db'</p>
<li>Running the API</li>
<p>python app.py</p>
</ol>

## License
licensed by MIT